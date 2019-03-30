from app import app
from flask import request


@app.route('/rating', methods=['GET'])
def get_rating():
    return "OK"


@app.route('/queue', methods=['GET'])
def queue():
    wwid = request.json.get('wwid', None)
    return "OK"
