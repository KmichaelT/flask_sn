import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app=Flask(__name__)
from twittest.core.routes import core
from twittest.error_pages.handlers import error_pages

#### DATABASE SETUP #######
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


db=SQLAlchemy(app)
Migrate(app,db)


#### LOGIN CONFIGS #######

login_manager=LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

from twittest.core.routes import core
from twittest.users.routes import users
from twittest.error_pages.handlers import error_pages
from twittest.feed.routes import posts


app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
app.register_blueprint(posts)
