import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
#from v1.auth.auth import AuthError, requires_auth
from flask_cors import CORS
from flask_migrate import Migrate
#from .config import *

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

from api import routes, models



#APP = create_app() #if i need to change variables i have to do that on environment level
#if __name__ == '__main__':
#    APP.run(host='0.0.0.0', port=8080, debug=True)