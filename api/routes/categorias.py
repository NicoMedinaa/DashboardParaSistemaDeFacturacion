from api import app
from api.models.categorias import Categorias
from flask import jsonify
from api.utils import token_required, client_resource, user_resources
from api.db.db import mysql

@app.route('/categoria')
def getAllCategorias():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM categoria') #WHERE id_user= {0}' .format(id_user))
    data = cur.fetchall() 
    lista=[]
    for row in data :
        objCategorias = Categorias(row)
        lista.append(objCategorias.to_json())
    return jsonify(lista)