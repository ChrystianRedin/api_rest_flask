from dataclasses import Field
from flask_marshmallow import Marshmallow
from models.auth_users import AuthUser
ma = Marshmallow()

class AuthUserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = AuthUser
    # Campos a mostrar
    #id_user_sys =  ma.auto_field()
    id_user = ma.auto_field()
    nombre_sistema = ma.auto_field()
    id_sistema =  ma.auto_field()
    created_at =  ma.auto_field()

auth_user_schema = AuthUserSchema()
auth_users_schema = AuthUserSchema(many=True)