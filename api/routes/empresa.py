from api import app
from api.models.empresa import Empresa
from flask import request,jsonify
from api.utils import token_required, client_resource, user_resources
from api.db.db import mysql

@app.route('/empresa/<string:empresa>')
def get_empresa(empresa):

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM empresa WHERE nombre = %s',(empresa,))
    data = cur.fetchall()
    empresa = []
    for row in data:
        objEmpresa = Empresa(row)
        empresa.append(objEmpresa.to_json())
    return jsonify({'Empresa': empresa})