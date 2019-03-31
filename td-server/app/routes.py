from app import app, mongo
from flask import request
from flask import jsonify
from database import create_tour_request


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
    create_tour_request(tour_name)
    mongo.db.tour.insert_one({"name": tour_name})
    return jsonify({'msg': "Success"}), 200

MAX_TOUR_COUNT = 100

def _in_top(table_id: int):
    if mongo.db.tour.find().sort({'score': -1}).limit(MAX_TOUR_COUNT).find({{'table_id': table_id}}):
        return True
    return False

def _get_top():
    return list(mongo.db.tour.find().sort({'score': -1}).limit(MAX_TOUR_COUNT))

def _get_current_list(table_id: int, near=3):
    cur = mongo.db.tour.find({'table_id': table_id})
    score = cur.pop()
    gte = mongo.db.tour.find({'score': {
        '$gte': curr.score,
        '$limit': near} 
        })
    lte =  mongo.db.tour.find({'score': {
        '$lte': curr.score,
        '$limit': near} 
        })
    return 

@app.route('/queue', methods=['GET'])
def queue():
    table_id = request.json.get('table_id', None)
    search = {'table_id': table_id}
    result = mongo.db.tour.find(search)
    if not result:
        return jsonify({'error': "Not found"}), 404
    in_top = _in_top(table_id)
    top_list = _get_top()
    if not in_top:
        current_list = _get_current_list()
    response = {'msg': "Success", 
    'in_top': in_top,
    'top_applications': top_list,
    'current': 

     }    
    return jsonify(), 200
