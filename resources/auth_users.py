# Flask RESTful
from http.client import SWITCHING_PROTOCOLS
from flask_restful import Resource, request
from flask_sqlalchemy import SQLAlchemy 
from cryptography.fernet import Fernet  
from models.auth_users import AuthUser
from schemas.auth_users import auth_user_schema, auth_users_schema

# Funcion para encriptar password
key = Fernet.generate_key()

db = SQLAlchemy()

# Recurso para Saber cual usuario del (colibri) esta entrando al sistema de documentos salientes
class AuthUserResource(Resource):
    def get(self, id_ext):
        user_id = db.session.query(AuthUser).filter(AuthUser.id_sistema==id_ext).first()
        return auth_user_schema.dump(user_id)
