# Flask RESTful
from http.client import SWITCHING_PROTOCOLS
from flask_restful import Resource, request
from flask_sqlalchemy import SQLAlchemy 
from cryptography.fernet import Fernet  
from models.user import User
from schemas.user import user_schema, users_schema

# Funcion para encriptar password
key = Fernet.generate_key()

db = SQLAlchemy()

class UserListResource(Resource):

    # Listado Usuario
    def get(self):
        users = User.query.all()
        print(users, flush=True)
        return users_schema.dump(users)

    # Crear Usuario
    def post(self):
        new_user = User(
            username=request.json["username"],
            email=request.json["email"],
            password=Fernet(key).encrypt(bytes(request.json["password"], "utf-8"))
        )
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user)


class UserResource(Resource):

    # Usuario por ID Interno
    def get(self, id_user):
        usuario_id = User.query.get_or_404(id_user)
        return user_schema.dump(usuario_id)

    # Actualizar Usuario
    def patch(self, id_user):
        update_user = User.query.get_or_404(id_user)
        db.session.commit()
        return user_schema.dump(update_user)
    
    # Eliminar Usuario
    def delete(self, id_user):
        delete_user = db.session.query(User).filter(User.id_user==id_user).first()
        db.session.delete(delete_user)
        db.session.commit()
        return user_schema.dump(delete_user)


