from flask import Flask
from flask_sqlalchemy import SQLAlchemy    
from sqlalchemy.dialects.postgresql import UUID
import uuid
import datetime

db = SQLAlchemy()

class Area(db.Model):
    __tablename__ = 'areas'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    
    def __repr__(self):
        return '<Area %r>' % self.nombre