from api import app
from api.models.empresa import Empresa
from flask import request,jsonify
from api.utils import token_required, client_resource, user_resources
from api.db.db import mysql