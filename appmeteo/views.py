#slide 47 du cour de python pour les commentaires  
from flask import *

app = Flask (__name__)

@app.route('/')
def index():

    data = {}

    data["nom_projet"] = "La météo dans les villes du monde !"

    data["titre_seo"]="Accueil - Météo"

    data["introduction"] = "Vous êtes dans le site de la meilleur météo Monde"
    return render_template('index.html', data=data)

    

@app.route('/equipe')
def equipe():

    data = {}

    data["nom_equipe"] = "Voici l'equipe"

    data["titre_seo"]="Equipe"

    data["ontro_equipe"] = "Vous êtes dans le site de la meilleur météo Monde"
    return render_template('equipe.html', data=data)

    