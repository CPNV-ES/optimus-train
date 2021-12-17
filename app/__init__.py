from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app)

@app.route("/trains")
def trains():
    value = {
        "company": "compagny1",
        "name": "train1",
        "weight": "999"
    }
    return value

@app.route("/schedules")
def schedules():
    value = {
        "date": "date1"
    }
    return value