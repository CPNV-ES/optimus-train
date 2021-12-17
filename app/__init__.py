from flask import Flask, jsonify
from flask_restx import Api
import requests

app = Flask(__name__)
api = Api(app)


@app.route("/trains")
def trains():
    response = requests.get(
        "https://data.sbb.ch/api/records/1.0/search/?dataset=jahresformation")

    json = response.json()

    return jsonify(json['records'])


@app.route("/schedules")
def schedules():
    value = {
        "date": "date1"
    }
    return value
