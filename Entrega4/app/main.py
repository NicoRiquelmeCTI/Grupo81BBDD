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

uri = "mongodb://grupo12:grupo12@gray.ing.puc.cl/grupo12"
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

# -------- Entrega 4 --------------

# Consulta por todos los correos
@app.route("/messages/")
def all_messages():
    mensajes = list(correos.find({},{"_id":0}))
    return json.jsonify({'result': 'Lista completa de correos', 'message': mensajes})

def project_search_message(nombre):
    qcorreos = list(correos.find({},{"_id":0}))
    proyectos_e = []
    for correo in qcorreos:
        if "receiver" in correo["metadata"].keys() or "sender" in correo["metadata"].keys():
            if correo["metadata"]["receiver"] == nombre or correo["metadata"]["sender"] == nombre:
                print(correo)
                proyectos_e.append(correo)
    return proyectos_e

#Consulta GET 1 y 2
@app.route("/messages/<mid>")
def get_message(mid):
    if mid == 'project-search':
        nombre = request.args.get('nombre')
        proyectos_e = project_search_message(nombre)
        if len(proyectos_e) > 0:
            return json.jsonify({'result': 'Correos relacionados a: {0}'.format(nombre), 'message': proyectos_e, "value": True})
        else:
            return json.jsonify({'result': 'correo no encontrado', "value": False})
        
    else:
        mensajes = list(correos.find({"id":mid}, {"_id":0}))
        if len(mensajes) > 0:
            return json.jsonify({'result': 'correo encontrado', 'message': mensajes, "value": True})
        else:
            return json.jsonify({'result': 'correo no encontrado', "value": False})


@app.route("/messages/<string:mid>", methods=['DELETE'])
def delete_message(mid):
    mensaje = list(correos.find({"id":mid}, {"_id":0}))
    if len(mensaje) > 0:
        correos.delete_one({"id": mid})
        mensaje = f"Correo id {mid} ha sido eliminado"
        return json.jsonify({'result': 'success', 'msn': mensaje})
    else:
        return json.jsonify({'result': 'El correo que intenta eliminar no existe'})

@app.route("/messages", methods=['POST'])
def new_message():
    msg_input = request.json
    if "content" not in msg_input.keys() or "metadata" not in msg_input.keys():
        return json.jsonify({'result': "el mensaje no fue incorporado porque no incluye el content o el metadata requeridos"})
    else:
        if "id" not in msg_input.keys():
            count = correos.count_documents({})
            msg_input["id"] = "correo"+str(count+1)
        data = {key: msg_input[key] for key in D_KEYS}
        if "time" not in data["metadata"].keys():
            return json.jsonify({'result': "el mensaje no fue incorporado porque el metadata no incluye el time"})
        else:
            resultado = correos.insert_one(data)
        if (resultado):
            msn = "Correo de id: {} creado con éxito".format(data["id"])
            success = True
        else:
            msn = "No se pudo crear el correo"
            success = False
        return json.jsonify({'result': success, 'msn': msn})

# Buscar correo segun nombre sender o receiver
@app.route("/messages/project-search/<string:receiver>")
def project_search_message_path(receiver):
    qcorreos = list(correos.find({},{"_id":0}))
    proyectos_e = []
    for correo in qcorreos:
        if "receiver" in correo["metadata"].keys() or "sender" in correo["metadata"].keys():
            if correo["metadata"]["receiver"] == receiver or correo["metadata"]["sender"] == receiver:
                print(correo)
                proyectos_e.append(correo)
    return json.jsonify({'result': 'Correos relacionados a: {0}'.format(receiver), 'message': proyectos_e})

@app.route("/messages/content-search/")
def content_search_message():
    content = request.json
    mensajes_d = []
    mensajes_r = []
    mensajes_f = []
    print(content)
    if len(content.keys()) == 0:
        return json.jsonify({'result': 'no existen restricciones, se muestran todos los correos', 'data': list(correos.find({},{"_id":0}))})
    else:
        if "desired" in content.keys():
            return json.jsonify({'result': 'Correos encontrados', 'data': list(correos.find({},{"_id":0}))})
        elif "required" in content.keys():
            textos = []
            espacio = " "
            for frase in content["required"]:
                textos.append("\"{}\"".format(frase))
            print(textos)
            mensajes_r = correos.find({"text": {"search": espacio.join(textos)}},{"_id":0})
            
        elif "forbidden" in content.keys():
            textos = []
            espacio = " "
            for frase in content["forbiden"]:
                textos.append("\"{}\"".format(frase))
            print(textos)
            mensajes_f = correos.find({"text": {"search": espacio.join(textos)}},{"_id":0})

        mns = mensajes_d+mensajes_r
        if intersection(mensajes_d, mensajes_r) in mns:
            mns.remove(intersection(mensajes_d, mensajes_r))
        elif mensajes_f in mns:
            mns.remove(mensajes_f)
        return json.jsonify({'result': 'Correos', 'message': list(mns)})


def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

if __name__ == "__main__":
    app.run()
