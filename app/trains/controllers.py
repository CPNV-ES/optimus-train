from flask import jsonify, Blueprint
import requests

mod_trains = Blueprint('trains', __name__, url_prefix='/trains')


@mod_trains.route('/', methods=['GET'])
def get_all_trains():
    response = requests.get(
        "https://data.sbb.ch/api/records/1.0/search/?dataset=jahresformation")

    json = response.json()

    return jsonify(json['records'])
