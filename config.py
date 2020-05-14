import os

class Config:
  '''
  config class to be inheritted by other class
  '''

  SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
  '''
  production config class
  '''

class DevConfig(Config):
  '''
  development config class
  '''

  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://billo:123456@localhost/sendit'

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