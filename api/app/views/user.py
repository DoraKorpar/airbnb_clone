from ..app import app
from flask import request

@app.route("/users", methods=["GET", "POST"])
def users():
	if request.method == "POST":
		pass

	elif request.method == "GET":
		pass

@app.route("/users/<user_id>", methods=["GET", "PUT", "DELETE"])
def users_id(user_id):
	pass
