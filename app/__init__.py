from flask import Flask
from flask_restx import Api
from flask import jsonify
import json

app = Flask(__name__)
api = Api(app)

# Trains
@app.route("/trains")
def trains():
    value = {
        "company": "compagny1",
        "name": "train1",
        "weight": "999"
    }
    return value

# Schedules
@app.route("/schedules")
def schedules():
    value = {
        "date": "date1"
    }
    return value

# Train lines
#   Return a list of train lines as json
@app.route("/lines")
def super():
    f = open('test_datas/test2.json')
    jsonData = json.loads(f.read())
    f.close()

    return (jsonify(jsonData["records"]))
