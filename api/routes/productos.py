from api import app
from api.models.productos import Productos
from flask import jsonify, request
from api.utils import token_required, client_resource, user_resources
from api.db.db import mysql

@app.route('/productos')
def get_all_Productos():
    #acceso a la db -> SELECT FROM ..
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos')
    data = cur.fetchall()
    print(cur.rowcount)
    print(data)
    productosList = []
    for row in data:
        objProductos = Productos(row)
        productosList.append(objProductos.to_json())
    return jsonify({"Productos": productosList})#render_template('lista.html', productos=productosList)##,jsonify(productosList)

@app.route('/productos/<int:id>', methods=['GET'])
def get_Productos_by_id(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE id = {0}'.format(id))
    data = cur.fetchall()
    print(cur.rowcount)
    print(data)
    if cur.rowcount >0 :
        objProductos =Productos(data[0])
        #acceso a BD -> SELECT FROM 
        return jsonify(objProductos.to_json()) #dato en tipo JSON   
    return jsonify({"message" : "id not found"})

@app.route('/productos', methods=['POST'])
def create_producto():
    body = request.get_json()
    codigo_barra = body['codigo_barra']
    # Verificar si el producto ya existe en la base de datos
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE codigo_barra = %s', (codigo_barra,))
    row = cur.fetchone()
    if row:
        return jsonify({"message" : "Producto ya registrado"}),400
    
    # Si el producto no existe, procede a insertarlo en la base de datos
    nombre = body['nombre']
    descripcion = body['descripcion']
    precio = body['precio']
    stock = body['stock']
    categoria = body['categoria']
    proveedor = body['proveedor']
    fecha_lanzamiento = body['fecha_lanzamiento']
    fecha_vencimiento = body['fecha_vencimiento']
    fecha_modificacion = body['fecha_modificacion']
    empresa = body['empresa']

    cur.execute('INSERT INTO productos (codigo_barra, nombre, descripcion, precio, stock, categoria, proveedor, fecha_lanzamiento, fecha_vencimiento, fecha_modificacion, empresa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (codigo_barra, nombre, descripcion, precio, stock, categoria, proveedor, fecha_lanzamiento, fecha_vencimiento, fecha_modificacion, empresa))
    cur.execute('SELECT LAST_INSERT_ID()')
    row = cur.fetchone()
    mysql.connection.commit()
    
    return jsonify({'id':row[0],'codigo_barra': codigo_barra, 'nombre':nombre, 'descripcion':descripcion, "precio":precio, "stock":stock, "categoria":categoria, "proveedor":proveedor, "fecha_lanzamiento":fecha_lanzamiento, "fecha_vencimiento":fecha_vencimiento, "fecha_modificacion":fecha_modificacion, "empresa":empresa})

@app.route('/productos/<int:id>', methods=['PUT'])
def update_productos(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE id = %s', (id,))
    rows= cur.fetchall()
    for row in rows:
        codigo_barra= row[1]
        nombre = row[2]
        descripcion = row[3]
        precio = row[4]
        stock = row[5]
        categoria = row[6]
        proveedor = row[7]
        fecha_lanzamiento = row[8]
        fecha_vencimiento = row[9]
        fecha_modificacion = row[10]
        empresa = row[11]
    
    body = request.get_json()
    # codigo_barra= body['codigo_barra']
    # nombre = body['nombre']
    # descripcion = body['descripcion']
    # precio = body['precio']
    # stock = body['stock']
    # categoria = body['categoria']
    # proveedor = body['proveedor']
    # fecha_lanzamiento = body['fecha_lanzamiento']
    # fecha_vencimiento = body['fecha_vencimiento']
    # fecha_modificacion = body['fecha_modificacion']
    # empresa = body['empresa']
    if body['codigo_barra'] != codigo_barra or body['nombre'] != nombre or body['descripcion'] != descripcion or body['precio'] != precio or body['stock'] != stock or body['categoria'] != categoria or body['proveedor'] != proveedor or body['fecha_lanzamiento'] != fecha_lanzamiento or body['fecha_vencimiento'] != fecha_vencimiento or body['fecha_modificacion'] != fecha_modificacion or body['empresa'] != empresa: 
    
    #acceso a la db -> SET  ---- WHERE ...
  #UPDATE SET ... WHERE ... 
        cur = mysql.connection.cursor()
        cur.execute('UPDATE productos SET nombre = %s, descripcion = %s, precio = %s,categoria = %s,proveedor = %s, stock = %s, fecha_lanzamiento = %s, fecha_vencimiento = %s, fecha_modificacion = %s, empresa = %s WHERE id = %s', (nombre,descripcion,precio,categoria,proveedor,stock,fecha_lanzamiento,fecha_vencimiento,fecha_modificacion,empresa, id))
        mysql.connection.commit()

        return jsonify({"id": id,
                        'nombre':nombre,
                        'descripcion':descripcion,
                        "precio":precio,
                        "stock":stock,
                        "categoria":categoria,
                        "proveedor":proveedor,
                        "fecha Lanzamiento":fecha_lanzamiento,
                        "fecha Vencimiento":fecha_vencimiento,
                        "fecha_modificacion":fecha_modificacion,
                        "empresa":empresa
                        })
    return jsonify({'message': 'no se realizo ningun cambio'})

@app.route('/productos/<int:id>', methods=['DELETE'])
def delete_productos(id):
    #acceso a la db -> DELETE FROM WHERE...

    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM productos WHERE id = {0}'.format(id))
    mysql.connection.commit()

    return jsonify({"message": "deleted", "id": id})