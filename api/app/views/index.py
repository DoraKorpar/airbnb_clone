from ..app import app
from flask_json import json_response
from ..models.base import database
import datetime

@app.route('/', methods=["GET"])
def index():
	utc = datetime.utcnow()
	now = datetime.datetime.now()
	return json_response(status='OK', utc_time=utc, time=now)

def before_request():
	database.connect()

def after_request():
	database.close()

def not_found():
	return json_response(code='404', msg='not found')
