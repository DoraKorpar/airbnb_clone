from peewee import *
from base import BaseModel
import hashlib

class User(BaseModel):
	email = CharField(128, null=False, unique=True)
	password = CharField(128, null=False)
	first_name = CharField(128, null=False)
	last_name = CharField(128, null=False)
	is_admin = BooleanField(default=False)

	def set_password(self, clear_password):
		m = hashlib.md5()
		self.password = m.update(clear_password)