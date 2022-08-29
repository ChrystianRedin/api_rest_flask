from flask import Flask
from flask_sqlalchemy import SQLAlchemy    
from sqlalchemy.dialects.postgresql import UUID

import uuid
import datetime

from models.area import Area

db = SQLAlchemy()

class AuthUser(db.Model):
    __tablename__ = 'usuario_sistemas'
    id_user_sys = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_user = db.Column(UUID(as_uuid=True))
    nombre_sistema = db.Column(db.String(80), unique=True, nullable=False)
    id_sistema = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)