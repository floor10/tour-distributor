import os

MONGO_HOST = os.environ.get('DB_HOST', '127.0.0.1')
MONGO_PORT = os.environ.get('DB_PORT', 27017)
MONGO_DB_NAME = os.environ.get('DB_NAME', 'employee_rating')


class BaseConfig:
    MONGO_URI = "mongodb://{}:{}/{}".format(MONGO_HOST, MONGO_PORT, MONGO_DB_NAME)
