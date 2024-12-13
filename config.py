import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-muito-secreta'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    DEBUG = FLASK_ENV == 'development'
