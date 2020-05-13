#Application factory

from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):

  app = Flask(__name__)

  #creating app configurations
  app.config.from_object(config_options[config_name])

  #initializing flask extensions
  #bootstrap
  bootstrap.init_app(app)
  #sqlalchemy
  db.init_app(app)
  #login
  login_manager.init_app(app)
  #Registering a Blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  #auth
  from .auth import auth
  app.register_blueprint(auth,url_prefix = '/authenticate')

  return app

