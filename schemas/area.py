from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemySchema
from models.area import Area
ma = Marshmallow()

class AreaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Area
        id = ma.auto_field()
        nombre = ma.auto_field()
        abreviacion = ma.auto_field()
        user_id = ma.auto_field()
    

area_schema = AreaSchema()
areas_schema = AreaSchema(many=True)