from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import  Api, Resource

from flask_cors import CORS
import config
from models.auth_users import AuthUser

# Models
from models.user import db
from models.area import db
from models.auth_users import db

# Resources
from resources.documentos import Documentos, Documento
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

# Documentos
api.add_resource(Documentos, '/documents')
api.add_resource(Documento, '/document/<string:id_doc>')

# Users
api.add_resource(UserListResource, '/api/users/')
api.add_resource(UserResource, '/api/user/<string:id_user>/')

# Auth User
api.add_resource(AuthUserResource, '/user_ext/<string:id_ext>')

