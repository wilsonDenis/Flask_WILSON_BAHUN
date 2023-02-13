from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    username = db.Column(db.String(15))
    is_active = db.Column(db.Boolean, default=False)
    
    def format(self):
        return {
            "id":self.id,
            "is_active":self.is_active
        } 