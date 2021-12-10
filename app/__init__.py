from flask import Flask
from flask_restx import Api
import json

app = Flask(__name__)
api = Api(app)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World mdr lol!</p>"

@app.route("/supermama")
def super():
    hihi = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
    return (str(hihi))
    #return json.dumps(hihi)
