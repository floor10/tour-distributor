from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config.from_object('app.config.BaseConfig')
mongo = PyMongo(app)

from app import routes
