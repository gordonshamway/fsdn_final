import os

FLASK_DEBUG = os.getenv('FLASK_DEBUG',True)
DEBUG = True
DEVELOPMENT = True
SECRET_KEY = 'do-i-really-need-this'
FLASK_SECRET = SECRET_KEY
DB_HOST = os.getenv('DB_HOST', 'localhost:5432')
DB_NAME = 'corona'
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
DB_URI = 'postgresql+psycopg2://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False