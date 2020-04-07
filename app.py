from zeep import Client
import requests
from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse

TOKEN = 'cb48489b-567a-4458-8525-517390fb1220'

app = Flask(__name__)
api = Api(app)



@app.route('/')
def index():
    return render_template('index.html')


 def week(i):
        switcher={
                0:'Sunday',
                1:'Monday',
                2:'Tuesday',
                3:'Wednesday',
                4:'Thursday',
                5:'Friday',
                6:'Saturday'
             }
         return switcher.get(i,"Invalid day of week")

class CalculerPrix(Resource):
     def prixdevise(devise,prix):
        dollar = 1.1
        francsuisse = 1.06
        bitcoin = 0.00012
        if devise == "euro":
            retour = prix
            pass
        elif devise == "dollar":
            retour = prix * dollar
            pass
        elif devise == "bitcoin":
            retour = prix * bitcoin
            pass
        elif devise == "francsuisse":
            retour = prix * francsuisse
            pass
        else:
            retour = "Erreur devise inconnue"
            pass
        return retour

    def get(self,distance,monnaie):
        PRIXKILOMETRE = 5
        #TODO devise
        prixtmp = float(distance) * PRIXKILOMETRE
        return prixdevise(monnaie,prixtmp)
        #return prixdevise(monnaie,prixtmp) + " " + monnaie

api.add_resource(CalculerPrix,'/API/calcul/<int:distance>/<string:monnaie>', endpoint = "calculPrix")

