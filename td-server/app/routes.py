from app import app, mongo
from flask import request
from flask import jsonify
from model import model


@app.route('/rating', methods=['GET'])
def get_rating():
    return jsonify({'msg': "Success"}), 200


@app.route('/applications', methods=['POST'])
def put_request():
    employee_id = request.json.get('employee_id', None)
    tour_type = request.json.get('tour_type', 'family')
    employee_family = request.json.get('employee_family', None)
    if employee_id:
        employee_pers_info = mongo.db.pers_info.find_one({'id': employee_id})
        score = model.compute_score(employee_pers_info, tour_type)

    mongo.db.requests.insert_one({'employee_id': employee_id,
                                  'score': score,
                                  'employee_family': employee_family,
                                  'tour_type': tour_type})

    return jsonify({'msg': "Successfully added"}), 200


@app.route('/put_tour', methods=['PUT'])
def put_request():
    tour_name = request.json.get('name', None)
    create_tour_request(tour_name)
    mongo.db.tour.insert_one({"name": tour_name})
    return jsonify({'msg': "Success"}), 200

MAX_TOUR_COUNT = 10

def _in_top(table_id: int):
    l = mongo.db.tour.find().sort({'score': -1}).limit(MAX_TOUR_COUNT)
    if l.find({{'table_id': table_id}}).count() == 0:
        return -1
    for i, v in enumerate(l):
        if v.get('table_id') and v.get('table_id') == table_id:
            return i
    return -1

def _get_top():
    return list(mongo.db.tour.find().sort({'score': -1}).limit(MAX_TOUR_COUNT))

def _get_current_list(table_id: int, near=3):
    cur = list(mongo.db.tour.find({'table_id': table_id}))
    if len(cur) != 1:
        return 
    score = cur.pop().get('score')
    # TODO fix unknown behavior
    gte = list(mongo.db.tour.find({'score': {
        '$gte': score,
        '$limit': near} 
        }))
    lte = list(mongo.db.tour.find({'score': {
        '$lte': score,
        '$limit': near} 
        }))
    return gte + cur + lte

@app.route('/queue', methods=['GET'])
def queue():
    table_id = request.json.get('table_id', None)
    search = {'table_id': table_id}
    result = mongo.db.tour.find(search)
    if not result:
        return jsonify({'error': "Not found"}), 404
    top_list = _get_top()
    current_list = []
    index_in_top = _in_top(table_id)
    in_top = False if index_in_top == -1 else True
    if not in_top:
        current_list = _get_current_list(table_id)
    response = {
    'in_top': in_top,
    'top_applications': top_list,
    'current': current_list,
    'index_in_top': index_in_top
    }
    return jsonify(response), 200
