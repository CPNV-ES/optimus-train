from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/trains")
def trains():
    return "<p>Trains's section</p>"

@app.route("/schedules")
def schedules():
    return "<p>schedules's section!</p>"
