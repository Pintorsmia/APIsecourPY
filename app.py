from zeep import Client
import requests
from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse

TOKEN = 'cb48489b-567a-4458-8525-517390fb1220'

app = Flask(__name__)
api = Api(app)


PRIXKILOMETRE = 5
dollar = 1.1
francsuisse = 1.06
bitcoin = 0.00012

@app.route('/')
def index():
    return render_template('index.html')

class CalculerPrix(Resource):
    def get(self,distance,monnaie):
        #TODO devise
        prixtmp = float(distance) * PRIXKILOMETRE
        switch (monnaie) {
        case "euro":
            result = prixtmp;
            break;
        case "dollar":
            result = dollar * prixtmp;
            break;
        case "francsuisse":
            result = francsuisse * prixtmp;
            break;
        case "bitcoin":
            result = bitcoin * prixtmp;
            break;
        default:
            return "Erreur devise inconnue";
            break;
    }
        return result + " " + monnaie

api.add_resource(CalculerPrix,'/API/calcul/<int:distance>/<string:monnaie>', endpoint = "calculPrix")

