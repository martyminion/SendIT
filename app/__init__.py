#Application factory

from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_simplemde import SimpleMDE


bootstrap = Bootstrap()
db = SQLAlchemy()
simple = SimpleMDE()

def create_app(config_name):

  app = Flask(__name__)

  #creating app configurations
  app.config.from_object(config_options[config_name])
  
  app.config['SECRET_KEY'] = 'any secret string'

  #initializing flask extensions
  #bootstrap
  bootstrap.init_app(app)
  #sqlalchemy
  db.init_app(app)
  simple.init_app(app)


  #Registering a Blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  #auth
  from .auth import auth
  app.register_blueprint(auth)

  return app

