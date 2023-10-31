from api import app
from api.models.productos import Productos
from flask import jsonify, request
from api.utils import token_required, client_resource, user_resources
from api.db.db import mysql

@app.route('/productos/<string:empresa>')
def get_all_Productos(empresa):

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE empresa = %s',(empresa,))
    data = cur.fetchall()
    print(cur.rowcount)
    print(data)
    productosList = []
    for row in data:
        objProductos = Productos(row)
        productosList.append(objProductos.to_json())
    return jsonify({"Productos": productosList})#render_template('lista.html', productos=productosList)##,jsonify(productosList)

@app.route('/productos/<string:empresa>/<int:id>', methods=['GET'])
def get_Productos_by_id(id,empresa):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE id = %s AND empresa = %s',(id, empresa))
    data = cur.fetchall()
    print(cur.rowcount)
    print(data)
    if cur.rowcount >0 :
        objProductos =Productos(data[0])
        #acceso a BD -> SELECT FROM 
        return jsonify(objProductos.to_json()) #dato en tipo JSON   
    return jsonify({"message" : "id not found"})

@app.route('/productos/<string:empresa>', methods=['POST'])
def create_producto(empresa):
    #print(type(empresa))
    body = request.get_json()
    codigo_barra = body['codigo_barra']

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE empresa = %s AND codigo_barra = %s',(empresa,codigo_barra))
    row = cur.fetchone()
    if row is not None:
        return jsonify({"message" : "Producto ya registrado"}),409
    
    nombre = body['nombre']
    empresa = empresa
    descripcion = body['descripcion']
    precio = body['precio']
    stock = body['stock']
    categoria = body['categoria']
    proveedor = body['proveedor']
    fecha_lanzamiento = body['fecha_lanzamiento']
    fecha_vencimiento = body['fecha_vencimiento']
    fecha_modificacion = body['fecha_modificacion']

    cur.execute('INSERT INTO productos (codigo_barra, nombre, descripcion, precio, stock, categoria, proveedor, fecha_lanzamiento, fecha_vencimiento, fecha_modificacion, empresa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (codigo_barra, nombre, descripcion, precio, stock, categoria, proveedor, fecha_lanzamiento, fecha_vencimiento, fecha_modificacion, empresa))
    cur.execute('SELECT LAST_INSERT_ID()')
    row = cur.fetchone()
    mysql.connection.commit()
    
    return jsonify({'codigo_barra': codigo_barra, 'nombre':nombre, 'descripcion':descripcion, "precio":precio, "stock":stock, "categoria":categoria, "proveedor":proveedor, "fecha_lanzamiento":fecha_lanzamiento, "fecha_vencimiento":fecha_vencimiento, "fecha_modificacion":fecha_modificacion, "empresa":empresa})

@app.route('/productos/<string:empresa>/<int:id>', methods=['PUT'])
def update_productos(id,empresa):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE id = %s AND empresa = %s', (id,empresa))
    row = cur.fetchone()
    if row is None:
        return jsonify({'message': 'Producto con ID {} no encontrado'.format(id)})
    id = row[0]
    codigo_barra = row[1]
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
    codigo_barraN= body['codigo_barra']
    nombreN = body['nombre']
    descripcionN = body['descripcion']
    precioN = body['precio']
    stockN = body['stock']
    categoriaN = body['categoria']
    proveedorN = body['proveedor']
    #fecha_lanzamientoN = body['fecha_lanzamiento']
    fecha_vencimientoN = body['fecha_vencimiento']
    #fecha_modificacionN = body['fecha_modificacion']
    empresaN = body['empresa']
    if str(codigo_barraN) != str(codigo_barra) or str(nombreN) != str(nombre) or str(descripcionN) != str(descripcion) or str(precioN) != str(precio) or str(stockN) != str(stock) or str(categoriaN) != str(categoria) or str(proveedorN) != str(proveedor) or str(empresaN) != str(empresa) or str(fecha_vencimientoN) != str(fecha_vencimiento):
        #acceso a la db -> SET  ---- WHERE ...
        #UPDATE SET ... WHERE ... 
        cur = mysql.connection.cursor()
        cur.execute('UPDATE productos SET codigo_barra = %s, nombre = %s, descripcion = %s, precio = %s,categoria = %s,proveedor = %s, stock = %s, fecha_vencimiento = %s, empresa = %s WHERE id = %s', (codigo_barraN,nombreN,descripcionN,precioN,categoriaN,proveedorN,stockN,fecha_vencimientoN,empresaN, id))
        mysql.connection.commit()

        return jsonify({"id": id,
                        'codigo_barra': codigo_barraN,
                        'nombre':nombreN,
                        'descripcion':descripcionN,
                        "precio":precioN,
                        "stock":stockN,
                        "categoria":categoriaN,
                        "proveedor":proveedorN,
                        "fecha Lanzamiento":fecha_lanzamiento,#siempre va a ser igual
                        "fecha Vencimiento":fecha_vencimientoN,
                        "fecha_modificacion":fecha_modificacion,#siempre va a ser igual
                        "empresa":empresaN,
                        'message': 'Cambios realizados con Exito'
                        })
    else:                    
        return jsonify({'message': 'no se realizo ningun cambio'})

@app.route('/productos/<int:id>', methods=['DELETE']) #preguntar por codigo de barras, el id solo es para nosotros
def delete_productos(id): 
    #acceso a la db -> DELETE FROM WHERE...
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE id = %s', (id,))
    row = cur.fetchone()
    if row is None:
        return jsonify({"message": 'El elemento no existe'})
    else:
        cur.execute('DELETE FROM productos WHERE id = {0}'.format(id))
        mysql.connection.commit()
        return jsonify({"message": "deleted", "id": id})