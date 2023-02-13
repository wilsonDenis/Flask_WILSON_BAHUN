"""from .auth import auth
from flask import Flask
from .views import views
from .models import db"""
#from siteweb import create_app
#import sys; print(sys.pathsys.path.append())
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from .models import db
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    from .models import User

    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def login_user(id):
       return User.query.get(int(id))
    return app

def create_database(app):
    if not path.exists('siteweb/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
    return app



