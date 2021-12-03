from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"
