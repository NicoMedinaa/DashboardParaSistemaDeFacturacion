from api import app
from api.models.proveedores import Proveedores
from flask import jsonify,request
from api.utils import token_required, client_resource, user_resources
from api.db.db import mysql


@app.route('/proveedor')
def get_all_proveedor():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM proveedor')
    data = cur.fetchall()
    print(cur.rowcount)
    print(data)
    proveedorList = []
    for row in data:
        objProveedor = Proveedores(row)
        proveedorList.append(objProveedor.to_json())
    return jsonify({"Proveedores": proveedorList})

@app.route('/proveedor/<int:id>', methods=['GET'])
def get_proveedor_by_id(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM proveedor WHERE id = {0}'.format(id))
    data = cur.fetchall()
    print(cur.rowcount)
    print(data)
    if cur.rowcount >0 :
        objProveedor =Proveedores(data[0])
        #acceso a BD -> SELECT FROM 
        return jsonify(objProveedor.to_json()) #dato en tipo JSON   
    return jsonify({"message" : "id not found"})

@app.route('/proveedor', methods=['POST'])
def create_proveedor():
    body = request.get_json()
    nombreProveedor = body['nombre']
    # Verificar si el producto ya existe en la base de datos
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM proveedor WHERE nombre = %s', (nombreProveedor,))
    row = cur.fetchone()
    if row:
        return jsonify({"message" : "Proveedor ya registrado"}),400
    
    # Si el producto no existe, procede a insertarlo en la base de datos
    nombre = body['nombre']
    direccion = body['direccion']
    telefono = body['telefono']
    email = body['email']
    descripcion = body['descripcion']

    cur.execute('INSERT INTO proveedor (nombre, direccion, telefono, email, descripcion) VALUES ( %s, %s, %s, %s, %s)', (nombre, direccion, telefono, email, descripcion))
    cur.execute('SELECT LAST_INSERT_ID()')
    row = cur.fetchone()
    mysql.connection.commit()
    
    return jsonify({'id':row[0], 'nombre':nombre, 'descripcion':descripcion, "telefono":telefono, "email":email, "descripcion":descripcion})

@app.route('/proveedor/<int:id>', methods=['PUT'])
def update_proveedor(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM proveedor WHERE id = %s', (id,))
    
    row=cur.fetchone()
    if row is None:
        return jsonify({'message': 'Proveedor con ID {} no encontrado'.format(id)})
    
    nombre = row[1]
    direccion = row[2]
    telefono = row[3]
    email = row[4]
    descripcion = row[5]
    
    body = request.get_json()
    #nombreN = body['nombre'] #es clave unica no se puede cambiar
    direccionN = body['direccion']
    telefonoN = body['telefono']
    emailN = body['email']
    descripcionN = body['descripcion']

    if str(descripcionN) != str(descripcion) or str(direccionN) != str(direccion) or str(telefonoN) != str(telefono) or str(emailN) != str(email):
        #cur = mysql.connection.cursor()
        cur.execute('UPDATE proveedor SET descripcion = %s, direccion = %s, telefono = %s, email = %s WHERE id = %s', (descripcionN, direccionN, telefonoN, emailN, id))
        mysql.connection.commit()
        #volver a leer asi mustro datos reales como el timeNow
        return jsonify({'id': id,
                        'nombre':nombre,
                        'descripcion':descripcionN,
                        'direccion':direccionN,
                        'telefono': telefonoN,
                        'email':emailN,
                        'message': 'Cambios realizados con Exito'
                        })
    else:                    
        return jsonify({'message': 'no se realizo ningun cambio'})

@app.route('/proveedor/<int:id>', methods=['DELETE']) #preguntar por codigo de barras, el id solo es para nosotros
def delete_proveedor(id): 
    #acceso a la db -> DELETE FROM WHERE...
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM proveedor WHERE id = %s', (id,))
    row = cur.fetchone()
    if row is None:
        return jsonify({"message": 'El elemento no existe'})
    else:
        cur.execute('DELETE FROM proveedor WHERE id = {0}'.format(id))
        mysql.connection.commit()
        return jsonify({"message": "deleted", "id": id})