from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'app_pass'

import api.routes.client
import api.routes.user
import api.routes.productos
import api.routes.categorias
import api.routes.empresa
import api.routes.servicios
import api.routes.proveedores