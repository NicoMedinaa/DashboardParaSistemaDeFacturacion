from api import app
from api.models.servicios import Servicios
from flask import jsonify,request
from api.utils import token_required, client_resource, user_resources
from api.db.db import mysql
from datetime import datetime

@app.route('/servicios')
def get_all_servicios():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM servicios')
    data = cur.fetchall()
    print(cur.rowcount)
    print(data)
    serviciosList = []
    for row in data:
        objServicios = Servicios(row)
        serviciosList.append(objServicios.to_json())
    return jsonify({"Productos": serviciosList})

@app.route('/servicios/<int:id>', methods=['GET'])
def get_servicios_by_id(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM servicios WHERE id = {0}'.format(id))
    data = cur.fetchall()
    print(cur.rowcount)
    print(data)
    if cur.rowcount >0 :
        objServicios =Servicios(data[0])
        #acceso a BD -> SELECT FROM 
        return jsonify(objServicios.to_json()) #dato en tipo JSON   
    return jsonify({"message" : "id not found"})

@app.route('/servicios', methods=['POST'])
def create_servicio():
    body = request.get_json()
    nombreServicio = body['nombre']
    # Verificar si el producto ya existe en la base de datos
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM servicios WHERE nombre = %s', (nombreServicio,))
    row = cur.fetchone()
    if row:
        return jsonify({"message" : "Servicio ya registrado"}),400
    
    # Si el producto no existe, procede a insertarlo en la base de datos
    nombre = body['nombre']
    descripcion = body['descripcion']
    precio = body['precio']
    duracion = body['duracion']
    categoria = body['categoria']
    unidadMedida = body['unidadMedida']
    fechaInicio = body['fechaInicio']
    fechaFinalizacion = body['fechaFinalizacion']
    #fechaCreacion = body['fechaCreacion']
    #fechaModificacion = body['fechaModificacion']
    empresa = body['empresa']
    estado = body['estado']

    cur.execute('INSERT INTO servicios (nombre, descripcion, precio, duracion, categoria, unidadMedida, fechaInicio, fechaFinalizacion, empresa, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (nombre, descripcion, precio, duracion, categoria, unidadMedida, fechaInicio, fechaFinalizacion, empresa, estado))
    cur.execute('SELECT LAST_INSERT_ID()')
    row = cur.fetchone()
    mysql.connection.commit()
    
    return jsonify({'id':row[0], 'nombre':nombre, 'descripcion':descripcion, "precio":precio, "duracion":duracion, "categoria":categoria, "unidadMedida":unidadMedida, "fechaInicio":fechaInicio, "fechaFinalizacion":fechaFinalizacion,"empresa":empresa, "estado":estado})

@app.route('/servicios/<int:id>', methods=['PUT'])
def update_servicios(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM servicios WHERE id = %s', (id,))
    rows = cur.fetchall()
    for row in rows:
        id = row[0]
        nombre = row[1]
        categoria = row[2]
        empresa = row[3]
        descripcion = row[4]
        precio = row[5]
        duracion = row[6]
        unidadMedida = row[7]
        fechaInicio = row[8]
        fechaFinalizacion = row[9]
        fechaCreacion = row[10]
        fechaModificacion = row[11]
        estado = row[12]
    
    body = request.get_json()
    nombreN = body['nombre']
    descripcionN = body['descripcion']
    precioN = body['precio']
    duracionN = body['duracion']
    categoriaN = body['categoria']
    unidadMedidaN = body['unidadMedida']
    fechaInicioN = body['fechaInicio']
    fechaFinalizacionN = body['fechaFinalizacion']
    #fechaCreacionN = body['fechaCreacion'] # Se crea una vez sola, en el alta del cliente
    #fechaModificacionN = body['fechaModificacion'] #es NOW
    empresaN = body['empresa']
    estadoN = body['estado']
    if str(nombreN) != str(nombre) or str(descripcionN) != str(descripcion) or str(precioN) != str(precio) or str(duracionN) != str(duracion) or str(categoriaN) != str(categoria) or str(unidadMedidaN) != str(unidadMedida) or str(empresaN) != str(empresa) or str(estadoN) != str(estado) or str(fechaInicioN) != str(fechaInicio) or str(fechaFinalizacionN) != str(fechaFinalizacion):
        #cur = mysql.connection.cursor()
        cur.execute('UPDATE servicios SET nombre = %s, descripcion = %s, precio = %s, categoria = %s, duracion = %s, unidadMedida = %s, fechaInicio = %s, fechaFinalizacion = %s, empresa = %s, estado = %s WHERE id = %s', (nombreN, descripcionN, precioN, categoriaN, duracionN, unidadMedidaN, fechaInicioN, fechaFinalizacionN, empresaN, estadoN, id))
        mysql.connection.commit()
        #volver a leer asi mustro datos reales como el timeNow
        return jsonify({"id": id,
                        'nombre':nombreN,
                        'descripcion':descripcionN,
                        "precio":precioN,
                        "duracion": duracionN,
                        "unidadMedida":unidadMedidaN,
                        "categoria":categoriaN,
                        "fechaInicioN":fechaInicioN,
                        "fechaFinalizacionN":fechaFinalizacionN,
                        "fechaCreacion":fechaCreacion,
                        "fechaModificacion": datetime.now(),
                        "empresa":empresaN,
                        "estado": estadoN,
                        'message': 'Cambios realizados con Exito'
                        })
    else:                    
        return jsonify({'message': 'no se realizo ningun cambio'})

@app.route('/servicios/<int:id>', methods=['DELETE']) #preguntar por codigo de barras, el id solo es para nosotros
def delete_servicios(id): 
    #acceso a la db -> DELETE FROM WHERE...
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM servicios WHERE id = %s', (id,))
    row = cur.fetchone()
    if row is None:
        return jsonify({"message": 'El elemento no existe'})
    else:
        cur.execute('DELETE FROM servicios WHERE id = {0}'.format(id))
        mysql.connection.commit()
        return jsonify({"message": "deleted", "id": id})