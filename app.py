from flask import Flask
from flask_restful import  Api
# Importacion de Rutas 
""" from routes.users import users_routes
from routes.documentos import documentos_routes
 """

from resources.apidocumentos import DocumentosLista, Documento

app = Flask(__name__)
api = Api(app)

# Registro de la ruta
""" app.register_blueprint(users_routes) """
""" app.register_blueprint(documentos_routes) """
api.add_resource(DocumentosLista, '/documents-list')
api.add_resource(Documento, '/document/<string:id_doc>')