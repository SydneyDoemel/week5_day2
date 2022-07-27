import os
basedir = os.path.abspath(os.path.dirname(__name__))
class Config():
    FLASK_APP = os.environ.get('FLASK_APP')
    FLAS_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')