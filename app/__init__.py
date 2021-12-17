from app.trains.controllers import mod_trains as trains_module
from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app)

app.register_blueprint(trains_module)
