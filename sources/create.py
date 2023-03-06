from utils.log import log
from utils.env import get_env
from utils.close import exit_app

try:
    from flask import Flask
    from flask_cors import CORS
    from flask_restful import Api
except ImportError as import_error:
    exit_app(f"Module not found: {import_error}")

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = get_env("DATABASE_URL")

CORS(app)
api = Api(app)
log.info("App created with basic cfg")