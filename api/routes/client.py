from api import app
from api.models.client import Cliente
from flask import jsonify
from api.utils import token_required, client_resource, user_resources
from api.db.db import mysql

# @app.route('/test')
# def test():
#     return jsonify({'ruta':'cliente-route'}) 
# 
# todas las rutas que hacen referencia a los recursos de los clintes..