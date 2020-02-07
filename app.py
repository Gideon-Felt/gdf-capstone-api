from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from environs import Env

app = Flask(__name__)
CORS(app)


env = Env()
env.read_env()

MONGO_URL_1 = env("MONGO_URL_1")
MONGO_URL_2 = env("MONGO_URL_2")

mongo1 = PyMongo(app, uri=MONGO_URL_1)
mongo2 = PyMongo(app, uri=MONGO_URL_2)
# mongo1 = PyMongo(app, uri = 'mongodb://127.0.0.1:27017/rdp_volume')
# mongo2 = PyMongo(app, uri = 'mongodb://127.0.0.1:27017/appraisal_volume')



@app.route('/rdps', methods=['GET'])
def get_all_rdps():
    ati = mongo1.db.ati

    output = []

    for rdp in ati.find():
        output.append({"street" : rdp['street'], "city" : rdp['city'], "state" : rdp['state'], "zip" : rdp['zip'], "latitude" : rdp['latitude'], "longitude" : rdp['longitude']})
    
    return jsonify({'results' : output})

@app.route('/rdps-by-state/<id>', methods=['GET'])
def get_rdps_by_state(id):
    ati = mongo1.db.ati

    output = []

    for rdp in ati.find({"state": id}):
        output.append({"street" : rdp['street'], "city" : rdp['city'], "state" : rdp['state'], "zip" : rdp['zip'], "latitude" : rdp['latitude'], "longitude" : rdp['longitude']})
    
    return jsonify({'results' : output})


@app.route('/appraisals', methods=['GET'])
def get_appraisals():
    dan_felt = mongo2.db.dan_felt

    output = []

    for apr in dan_felt.find():
        output.append({"file_no" : apr["file_no"], "street" : apr['street'], "city" : apr['city'], "state" : apr['state'], "zip" : apr['zip'], "effective_date" : apr["effective_date"], "appraised_value" : apr["appraised_value"], "latitude" : apr['latitude'], "longitude" : apr['longitude']})
    
    return jsonify({'results' : output})


@app.route('/appraisals-by-state/<id>', methods=['GET'])
def get_appraisals_by_state(id):
    dan_felt = mongo2.db.dan_felt

    output = []

    for apr in dan_felt.find({"state": id}):
        output.append({"file_no" : apr["file_no"], "street" : apr['street'], "city" : apr['city'], "state" : apr['state'], "zip" : apr['zip'], "effective_date" : apr["effective_date"], "appraised_value" : apr["appraised_value"], "latitude" : apr['latitude'], "longitude" : apr['longitude']})
    
    return jsonify({'results' : output})


if __name__=='__main__':
    app.run(debug=True)