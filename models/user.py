from flask import Flask
from flask_sqlalchemy import SQLAlchemy    
from sqlalchemy.dialects.postgresql import UUID


import uuid
import datetime


from models.area import Area


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id_user = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
   
    #area = db.relationship('Area', backref='user', lazy=True)



