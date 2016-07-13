from ..app import app
from flask import request
from ..models.base import database
from peewee import *

@app.route("/users", methods=["GET", "POST"])
def users():
	if request.method == "POST":
		entry = User.insert()
		entry.execute()

	elif request.method == "GET":
		

@app.route("/users/<user_id>", methods=["GET", "PUT", "DELETE"])
def users_id(user_id):
	if request.method == "GET":
		pass

	elif request.method == "PUT":
		pass

	elif request.method == "DELETE":
		pass
