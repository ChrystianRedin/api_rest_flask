from dataclasses import Field
from flask_marshmallow import Marshmallow
from models.user import User
ma = Marshmallow()

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
    # Campos a mostrar
    id_user =  ma.auto_field()
    username =  ma.auto_field()
    email =  ma.auto_field()
    activo =  ma.auto_field()
    created_at =  ma.auto_field()

user_schema = UserSchema()
users_schema = UserSchema(many=True)