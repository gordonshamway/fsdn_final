import os

class DevConfig(object):
    FLASK_DEBUG = os.getenv('FLASK_DEBUG',True)
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'do-i-really-need-this'
    FLASK_SECRET = SECRET_KEY
    DB_HOST = os.getenv('DB_HOST', 'localhost:5432')
    DB_NAME = 'corona2'
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
    #DB_URI = os.getenv('DB_URI', 'postgresql+psycopg2://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME))
    DB_URI='postgres://idvhfrtawyknop:35081e3febb224ec06731be10116283280342b6cd065da713cf26a40832081bc@ec2-34-195-169-25.compute-1.amazonaws.com:5432/da46k1e0drjj5l'
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(DevConfig):
    DB_NAME = 'corona_test'
    DB_USER = os.getenv('TEST_DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('TEST_DB_PASSWORD', 'postgres')
    DB_HOST = os.getenv('TEST_DB_HOST', 'localhost:5432')
    #DB_URI = os.getenv('DB_URI', 'postgresql+psycopg2://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME))
    DB_URI='postgres://idvhfrtawyknop:35081e3febb224ec06731be10116283280342b6cd065da713cf26a40832081bc@ec2-34-195-169-25.compute-1.amazonaws.com:5432/da46k1e0drjj5l'
    SQLALCHEMY_DATABASE_URI = DB_URI