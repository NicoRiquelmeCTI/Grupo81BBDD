from flask import Flask, render_template, request, abort, json
from pymongo import MongoClient
import pandas as pd
import os
import atexit
import subprocess

#Instanciar las llaves del documento
D_KEYS = ["id", "content", "metadata"]
METADATA_KEYS = ["time", "sender", "receiver"]

#Levantar servidor de Mongo
mongod = subprocess.Popen("mongod", stdout=subprocess.DEVNULL)

uri = "mongodb://grupo58:grupo58@gray.ing.puc.cl/grupo58"
# La uri 'estándar' es "mongodb://user:password@ip/database"
atexit.register(mongod.kill)
client = MongoClient(uri)
db = client.get_database()

#Seleccionar colección de correos
correos = db.correos

#Instanciar aplicación de Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Bienvenido</h1>"

@app.route("/message/<string:mid>")
def get_message(mid):
    mensajes = list(correos.find(mid))
    return json.jsonify(mensajes)

@app.route("/message/<string:id>", methods=['DELETE'])
def delete_message(id):
    correos.delete_one({"id": id})
    mensaje = f"Correo id {id} ha sido eliminado"
    return json.jsonify({'result': 'success', 'msn': mensaje})

@app.route("/message/", methods=['POST'])
def new_message():
    return

@app.route("/messages/project-search<string:receiver>")
def project_search_message(receiver):

    return

@app.route("/messages/content-search<string:content>")
def content_search_message(content):
    return

if __name__ == "__main__":
    app.run()
