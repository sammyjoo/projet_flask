#slide 47 du cour de python pour les commentaires  
from flask import *

#importation de l'heure
import datetime


app = Flask (__name__)

#importation des variables du fichier config.py
app.config.from_object('config')

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

    

@app.route('/equipe')
def equipe():

    data = {}

    data["nom_equipe"] = "Voici l'equipe"
    data["titre_seo"]="Equipe"
    data["nom_de_la_societe"] = app.config['NOM_SOCIETE']
    data["ontro_equipe"] = "Vous êtes dans le site de la meilleur météo Monde"

    data["developpeurs"] = ["alexandre", "laureen", "jojo le plus beau"]

    return render_template('equipe.html', data=data)

    