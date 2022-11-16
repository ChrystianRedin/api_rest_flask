from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import  Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint

from flask_cors import CORS
import config
from models.auth_users import AuthUser

# Models
from models.user import db
from models.area import db
from models.auth_users import db

# Resources
from resources.documentos import Documentos, Documento, Documento_Id_User
from resources.users import UserListResource, UserResource
from resources.auth_users import AuthUserResource


# Configuracion Flask
app = Flask(__name__)

# SQLAlchemy
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db-docs/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

# SWAGGER Configs
SWAGGER_URL= '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'API Documentos Salientes'
    }
)


app.register_blueprint(SWAGGER_BLUEPRINT,url_prefix = SWAGGER_URL)

# Documentos
api.add_resource(Documentos, '/documents')
api.add_resource(Documento_Id_User, '/documents/<string:id_user>')
api.add_resource(Documento, '/document/<string:id_doc>')

# Users
api.add_resource(UserListResource, '/api/users')
api.add_resource(UserResource, '/api/user/<string:id_user>')

# Auth User
api.add_resource(AuthUserResource, '/api/user_ext/<string:id_ext>')

