from ..app import app
from flask import request
from flask_json import json_response
from ..models.base import database
from peewee import *

@app.route("/users", methods=["GET", "POST"])
def users():
	if request.method == "POST":
		data = request.data
		first_name = data['first_name']
		last_name = data['last_name']
		email = data['email']
		password = data['password']

		entry = User.insert(first_name=first_name, last_name=last_name, email=email, password=User.set_password(password))
		entry.execute()

		user = User.select().where(first_name=first_name, last_name=last_name, email=email).get()
		return json.dumps(user.to_hash())

	elif request.method == "GET":
		list_users = User.select()
		return json.dumps(list_users.to_hash())

@app.route("/users/<user_id>", methods=["GET", "PUT", "DELETE"])
def users_id(user_id):
	if request.method == "GET":
		user = User.select().where(id=users_id).get()
		return json.dumps(user.to_hash())

	elif request.method == "PUT":
		pass

	elif request.method == "DELETE":
		pass
