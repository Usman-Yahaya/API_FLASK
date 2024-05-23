# save this as app.py
# from glob import escape
# from urllib import request
from flask import Flask
import requests

app = Flask(__name__)

# @app.route("/Mon_api")
# def hello():
    # array = [1,2,3,4,5,6,7,8]
    # for i in [1,2,3,4,5,6,7] :
    #     return ("la valeur est : " + i)
    # return 'Bonjour'

# app.run()

# @app.route("/Mon_api1")
# def hello():
    
#     return 'Bonjour'

# app.run()

@app.route("/Bonjour/<name>")
def hello(name):
    
    
    print(jason_recuperer1)

    try:
        pikachu_data = requests.get('https://pokeapi.co/api/v2/pokemon/'+ name)
        jason_recuperer1 = pikachu_data.json()
        if(jason_recuperer1):
            return 'True'
    except:
        return 'Vous etes un grand dev'

        
        
# app.run(debug=True)

@app.route('/recherche/<univers>/<identifiant>')
def recherche(univers, identifiant):
    if univers == 'sw' :
        swapi = requests.get('https://swapi.dev/api/people/' + identifiant)
        s_value =swapi.json()
        return s_value

    if univers == 'pk' :
        pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/' + identifiant)
        p_value = pokemon.json()
        return p_value
    else : 
        return 'Erreur du la  requete'


app.run(debug=True)

class voiture :
    def __init__(self, couleur, model, vitesse):
        self.couleur = couleur
        self.model = model
        self.vitesse = vitesse
    def add_voiture(self, marque) :
        self.marque = marque
        # self.couleur = couleur
        # self.model = model
        # self.vitesse = vitesse

voitur = voiture('Rouge', '')
        
        