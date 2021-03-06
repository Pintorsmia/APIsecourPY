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

class CalculerPrix(Resource):
    def get(self,distance,devise):
        PRIXKILOMETRE = 5
        dollar = 1.1
        francsuisse = 1.06
        bitcoin = 0.00012
        
        prixtmp = float(distance) * PRIXKILOMETRE
        if devise == "euro":
            prix = round(prixtmp,2)
        elif devise == "dollar":
            prix = round(prixtmp * dollar,2)
        elif devise == "francsuisse":
            prix = round(prixtmp * francsuisse,2)
        elif devise == "bitcoin":
            prix = prixtmp * bitcoin
        else :
            return{'message' : 1}
        return {'message' : 0, 'prix' : prix, 'devise' : devise}
        #return prixdevise(monnaie,prixtmp) + " " + monnaie

api.add_resource(CalculerPrix,'/API/calcul/<string:distance>/<string:devise>', endpoint = "calculPrix")

