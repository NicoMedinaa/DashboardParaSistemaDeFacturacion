from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL
from categorias import Categorias
from proveedores import Proveedores
from productos import Productos

import datetime

#from markupsafe import escape


app = Flask(__name__) #construcor de la clase, creamos una app con este paquete

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Admin'# nombre dew usuario elejido
app.config['MYSQL_PASSWORD'] ='432287' # contra elejida
app.config['MYSQL_DB'] = 'comercio'
app.config['SECRET_KEY'] = 'app_pass'
app.config['STATIC_FOLDER'] = 'static' # para servir tu aplicación web y necesitas servir archivos estáticos

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/productos')
def get_all_PrProductoss():
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
    #acceso a BD -> SELECT FROM 
    return jsonify(productosList)

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
    nombre = body['nombre']
    descripcion = body['descripcion']
    precio = body['precio']
    stock = body['stock']
    categoria = body['categoria']
    proveedor = body['proveedor']
    fecha_lanzamiento = body['fecha_lanzamiento']
    fecha_vencimiento = body['fecha_vencimiento']
    
    # acceso a la db -> 
    cur = mysql.connection.cursor()
    #Control si existye el nombre endicado
    cur.execute('SELECT * FROM productos WHERE Nombre = %s', (nombre,))
    row = cur.fetchone()
    if row:
        return jsonify({"message" : "producto ya registrado"})
    #INSERT INTO .. control de variables..
    cur.execute('INSERT INTO productos (Nombre, Descripción, Precio, Stock, Categoría, Proveedor, Fecha_Lanzamiento, Fecha_Vencimiento) VALUES (%s, %s, %s, %s,%s, %s, %s, %s)', (nombre,descripcion,precio,stock,categoria,proveedor,fecha_lanzamiento,fecha_vencimiento))
    mysql.connection.commit()
    # Obtener el id del registro creado
    cur.execute('SELECT LAST_INSERT_ID()')
    row = cur.fetchone()
    print(row[0])
    
    return jsonify({"id": row[0],
                    'Nombre':nombre,
                    'Descripcion':descripcion,
                    "Precio":precio,
                    "Stock":stock,
                    "Categoria":categoria,
                    "Proovedor":proveedor,
                    "Fecha Lanzamiento":fecha_lanzamiento,
                    "Fecha Vencimiento":fecha_vencimiento
                    })


if __name__ == '__main__':
    app.run(debug=True,port=5000)