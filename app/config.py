import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = False
    TESTING = False
    
class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///development.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REMEMBER_COOKIE_DURATION = 604800
class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = 'sqlite:///testing.db'