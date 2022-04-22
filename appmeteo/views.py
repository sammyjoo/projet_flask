#slide 47 du cour de python pour les commentaires  
from crypt import methods
from urllib import request
from flask import *
import requests
import json
from flask_sqlalchemy import SQLAlchemy

#importation de l'heure
import datetime

#importer wikiscraper
import wikiscraper as ws
ws.lang("fr")

app = Flask (__name__)

#importation des variables du fichier config.py
app.config.from_object('config')


#DÉBUT DE LA BDD
# configuration du chemin de notre BDD
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///equipe.db"
#Init de l'obejt pour la BDD
db = SQLAlchemy(app)

#Création du modèle (unique dans notre exemple)
class Equipe(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nom=db.Column(db.String(255), nullable=False)
    prenom=db.Column(db.String(255), nullable=False)
    email=db.Column(db.String(255), nullable=False)
#Pour générer le fichier .db à partir du modèle
db.create_all()
#FIN DE LA BDD



@app.route('/')
def index():

    data = {}

    data["nom_projet"] = "La météo dans les villes du monde !"
    data["titre_seo"]="Accueil - Météo"
    data["introduction"] = "Vous êtes dans le site de la meilleur météo Monde"
    
    #configuration de l'heure actuelle
    time = datetime.datetime.now()
    data["heure_actuelle"] = time.hour

    return render_template('index.html', data=data)

    
#ajouter la methods pour que la page fonctionne. recevoir des donnée (POST ET GET)
@app.route('/equipe/', methods=['GET', 'POST'])
def equipe():

    data = {}

    data["nom_equipe"] = "Voici l'equipe"
    data["titre_seo"]="Equipe"
    data["nom_de_la_societe"] = app.config['NOM_SOCIETE']

#pour ajouter un nouveau champs, supprimer la bdd "equipe.db" pour reinit à zero la bdd
    if request.method == "POST":
        prenom_dev = request.form.get("prenom")

        if request.method== "POST":
            email_dev = request.form.get("email")
    

        if request.form.get("nom") =="":
            nom_dev = "non rensigné"
        else :
            nom_dev = request.form.get('nom')

        requete_ajout1 = Equipe(nom=nom_dev, prenom=prenom_dev, email=email_dev)
        db.session.add(requete_ajout1)
        db.session.commit()

    data["developpeurs"]= Equipe.query



    data["ontro_equipe"] = "Vous êtes dans le site de la meilleur météo Monde"

    

    return render_template('equipe.html', data=data)

@app.route('/meteo/', methods=['GET'])
def meteo():
    #récupère le nom de la ville avec GET 
    #ATTENTION avec POST on met "form" au lieu de "args"
    ville = request.args.get("ville")

    if not ville:
        return redirect('/')
    else:


        #avec la ville, on fait la requete vers l'API openweather
        reponse = requests.get(
            #requete + variable ville + API
        "http://api.openweathermap.org/data/2.5/weather?q="+ville+"&units=metric&appid="+app.config['KEY_API'])

        #on fait appel au JSON
        data = reponse.json()
        print(data)


        ville = data["name"]

        #température
        temperature = round(data["main"]['temp'])



        #vent
        vent = round(data["wind"]["speed"] * 3.6, 1)
        "le vent est à"+" "+str(vent)+"km/h"
        #humidité
        humidite = data["main"]["humidity"]


        data["temperature"]='temperature à '+str(ville)+" "+str(temperature)+" "+'degré' 

        data["vent"]="le vent est à"+" "+str(vent)+"km/h"

        data["humidite"]=str(humidite)+"% d'humidités"

        data["nom_ville"] = ville




    
        #renvoi les information dans le navigateur
        return render_template('meteo.html', data=data)


@app.route('/ville/<nom>')
def ville_info(nom):
    data ={}
    data["nom_ville"] = nom

    result = ws.searchBySlug(nom)

    data["wiki_paragraphe"]= result.getAbstract()
    img=result.getImage()
    data["wiki_image"] = img[0]

    return render_template('ville_info.html', data=data)

@app.errorhandler(404)
def notFound(error):
    return "erreur 404 :("