from functools import wraps
from flask import request, jsonify
import jwt
from api import app
from api.db.db import mysql

def token_required(func):
    @wraps(func)
    def decorated(*args,**kwargs):
        print(kwargs)
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']#se puede poner HTTP headers personalizados pero tmb tenemos q cambiarlo en el trundle
        
        if not token:
            return jsonify({'message':'Falta el TOKEN'}),401
        
        user_id =None
        if 'user-id' in request.headers:
            user_id = request.headers['user-id']
        if not user_id:
            return jsonify({'message': 'Falta el usuario'}),401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms = ['HS256'])
            exp = data['exp']
            id_token = data['id']
            if int(user_id) != int(id_token):
                return jsonify({'message': 'Error de id'}),401
            #agregar que un usuario no puede ingresar con el token de otro usuario
        except Exception as e:
            print(e)
            return jsonify({'message': str(e)}),401
        
        return func(*args,**kwargs)
    return decorated

def client_resource(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        print("Argumento en client_resource",kwargs)
        id_cliente = kwargs['id_client']
        cur = mysql.connection.cursor()
        cur.execute('SELECT id_user FROM client WHERE id = {0}'.format(id_cliente)) 
        data = cur.fetchone()
        if data:
            id_prop = data[0]
            user_id = request.headers['user-id']
            if int(id_prop) != int(user_id):
                return jsonify({'message': 'No tiene permisos para acceder a este recurso'}),401
        return func(*args, **kwargs)
    return decorated

def user_resources(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        print("Argumento en users_resource",kwargs)
        id_user_route = kwargs['id_user']
        user_id = request.headers['user-id']
        if int(id_user_route) != int(user_id):
            return jsonify({'message': 'No tiene permisos para  acceder a este recurso'}),401
        return func(*args, **kwargs)
    return decorated