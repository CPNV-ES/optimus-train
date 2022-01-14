from flask import jsonify, Blueprint
import requests

mod_trains = Blueprint('trains', __name__, url_prefix='/trains')

translated_keys = {
    'zug':          'train_number',
    'zns':          'train_numbering_system',
    'vp' :          'transport_period',
    'debicode' :    'debtor_code',
    'zugart' :      'train_type',
    'suf' :         'suffix',
    'traktion' :    'traction',
    'bhf_von' :     'from_station',
    'von' :         'departure_time',
    'bhf_bis' :     'to_station',
    'bis' :         'arrival_time',
    'umlauf' :      'rotation',
    'von0' :        'rotation_start_time',
    'bis0' :        'rotation_end_time',
    'tl' :          'daily_runs',
    'tl_vp' :       'daily_runs_transport_period',
    '11' :          'nb_runs_on_monday',
    '22' :          'nb_runs_on_tuesday',
    '33' :          'nb_runs_on_wednesday',
    '44' :          'nb_runs_on_thursday',
    '55' :          'nb_runs_on_friday',
    '66' :          'nb_runs_on_saturday',
    '77' :          'nb_runs_on_sunday',
    'block_bezeichnung' : 'block_designation',
    'vp_zug_spallte_c' : 'transport_period_c',
    'vp_tagesleistung_spaltte_r' : 'daily_runs_r',
    'beginnfahrplanperiode' : 'timetable_period_start'
}

keys_containing_days = ['transport_period_c', 'daily_runs_r']

translated_days = {
    'Mo' : 'Mon',
    'Di' : 'Tur',
    'Mi' : 'Wed',
    'Do' : 'Thu',
    'Fr' : 'Fri',
    'Sa' : 'Sat',
    'So' : 'Sun'
}

@mod_trains.route('/', methods=['GET'])
def get_all_trains():
    response = requests.get(
        "https://data.sbb.ch/api/records/1.0/search/?dataset=jahresformation")

    json = response.json()
    out_entries = []
    for row in json['records']:
        fields = row['fields']
        f = {}
        
        for k in fields:
            if k in translated_keys:
                tk = translated_keys[k]
                f[tk] = fields[k]
                if tk in keys_containing_days:
                    for ger, eng in translated_days.items():
                        f[tk] = f[tk].replace(ger, eng)
        
        out_entries.append({
            'fields' : f,
            'record_timestamp' : row['record_timestamp'],
            'record_id' : row['recordid']
        })

    return jsonify(out_entries)
