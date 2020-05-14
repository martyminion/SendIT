import os

class Config:
  '''
  config class to be inheritted by other class
  '''

  SECRET_KEY = os.environ.get('SECRET_KEY')
  #email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
class ProdConfig(Config):
  '''
  production config class
  '''

class DevConfig(Config):
  '''
  development config class
  '''

  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin:kimani@localhost/sendit'
  DEBUG = True


  ##change the username to your username and password


class TestConfig(Config):
  '''
  tests config class
  '''

config_options = {
  'development': DevConfig,
  'production': ProdConfig,
  'tests': TestConfig
}