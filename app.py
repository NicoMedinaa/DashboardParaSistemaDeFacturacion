from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL
from flask_cors import CORS
from categorias import Categorias
from proveedores import Proveedores
from productos import Productos
from servicios import Servicios
from empresa import Empresa

import datetime

#from markupsafe import escape


app = Flask(__name__) #construcor de la clase, creamos una app con este paquete
CORS(app)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Admin'# nombre dew usuario elejido
app.config['MYSQL_PASSWORD'] ='432287' # contra elejida
app.config['MYSQL_DB'] = 'sistemafacturacion'
app.config['SECRET_KEY'] = 'app_pass'
app.config['STATIC_FOLDER'] = 'static' # para servir tu aplicación web y necesitas servir archivos estáticos

mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT nombre FROM categoria')
    categorias = cur.fetchall()
    cur.execute('SELECT nombre FROM proveedor')
    proveedores = cur.fetchall()
    cur.execute('SELECT nombre FROM empresa')
    empresas = cur.fetchall()
    return render_template('./index.html', categorias=categorias, proveedores=proveedores,empresas=empresas)


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
    return render_template('lista.html', productos=productosList)##,jsonify(productosList)

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
    id = body['id']
    # Verificar si el producto ya existe en la base de datos
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE id = %s', (id,))
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

    cur.execute('INSERT INTO productos (id,nombre, descripcion, precio, stock, categoria, proveedor, fecha_lanzamiento, fecha_vencimiento,fecha_modificacion,empresa) VALUES (%s,%s, %s, %s, %s,%s, %s, %s, %s, %s, %s)', (id, nombre, descripcion, precio, stock, categoria, proveedor, fecha_lanzamiento, fecha_vencimiento, fecha_modificacion, empresa))
    mysql.connection.commit()
    
    return jsonify({"id": id, 'nombre':nombre, 'descripcion':descripcion, "precio":precio, "stock":stock, "categoria":categoria, "proveedor":proveedor, "fecha_lanzamiento":fecha_lanzamiento, "fecha_vencimiento":fecha_vencimiento, "fecha_modificacion":fecha_modificacion, "empresa":empresa})

@app.route('/productos/<int:id>', methods=['PUT'])
def update_productos(id):
    body = request.get_json()
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


@app.route('/productos/<int:id>', methods=['DELETE'])
def delete_productos(id):
    #acceso a la db -> DELETE FROM WHERE...

    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM productos WHERE id = {0}'.format(id))
    mysql.connection.commit()

    return jsonify({"message": "deleted", "id": id})


if __name__ == '__main__':
    app.run(debug=True,port=5000)