from api import app
from api.models.client import Cliente
from flask import jsonify,request
from api.utils import token_required, client_resource, user_resources
from api.db.db import mysql

@app.route('/cliente/<string:empresa>', methods=['GET'])
def get_all_clients(empresa):
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM cliente') #WHERE id_user= {0}' .format(id_user))
    data = cur.fetchall()
    clientList = []
    # de la fila extraigo los datos para crear un objeto y luego con esos crear un JSON
    for row in data :
        objClient = Cliente(row)
        clientList.append(objClient.to_json())
    #retorna una lista de JSON sss
    #Finalmente, la lista de objetos JSON se devuelve como respuesta. 
    #Flask automáticamente convierte esta lista de objetos JSON en una respuesta HTTP con formato JSON.
    return jsonify(clientList)


@app.route('/cliente/<string:empresa>', methods=['POST'])
def agregar_cliente(empresa):
    body = request.get_json()
    nombre = body['nombre']
    dni = body['dni']
    direccion = body['direccion']
    telefono = body['telefono']
    email = body['email']
    #fechaRegistro = body['fechaRegistro']

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cliente WHERE dni = %s AND nombre = %s',(dni,nombre))
    row = cur.fetchone()
    if row is not None: #verificar
        return jsonify({"message" : "Cliente ya registrado"}),404


    cur.execute('INSERT INTO cliente (dni,nombre,direccion,telefono,email) VALUES (%s, %s, %s, %s, %s)', (dni,nombre,direccion,telefono,email))
    cur.execute('SELECT LAST_INSERT_ID()')
    row = cur.fetchone()
    mysql.connection.commit()

    return jsonify({'dni': dni, 'nombre':nombre})