from flask import Flask
from flask_restful import  Api
# Importacion de Rutas 
from routes.users import users_routes
# Recursos Documentos
from resources.documentos import Documentos, Documento
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

# Registro de la ruta
app.register_blueprint(users_routes)

# Documentos
api.add_resource(Documentos, '/documents')
api.add_resource(Documento, '/document/<string:id_doc>')