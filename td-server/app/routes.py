from app import app, mongo
from flask import request
from flask import jsonify


@app.route('/rating', methods=['GET'])
def get_rating():
    return jsonify({'msg': "Success"}), 200


@app.route('/put_employee', methods=['PUT'])
def put_request():
    employee_name = request.json.get('name', None)
    mongo.db.employee.insert_one({"name": employee_name})
    return jsonify({'msg': "Success"}), 200


@app.route('/put_tour', methods=['PUT'])
def put_request():
    tour_name = request.json.get('name', None)
    mongo.db.tour.insert_one({"name": tour_name})
    return jsonify({'msg': "Success"}), 200


@app.route('/queue', methods=['GET'])
def queue():
    wwid = request.json.get('wwid', None)
    return jsonify({'msg': "Success"}), 200
