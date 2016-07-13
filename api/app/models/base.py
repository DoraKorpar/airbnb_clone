import peewee
import datetime
from ....config import *

# variable database linked to DATABASE imported from config file
database = peewee.MySQLDatabase(DATABASE)

class BaseModel(peewee.Model):
	id = peewee.PrimaryKeyField(unique=True)
	created_at = peewee.DateTimeField(default=datetime.datetime.now())
	updated_at = peewee.DateTimeField(default=datetime.datetime.now())

	# overloads save method of Model to update updated_at before saving
	def save(self, *args, **kwargs):
		self.updated_at = datetime.datetime.now()
		return super(BaseModel, self).save(*args, **kwargs)

	class Meta:
		database = database
		order_by = ("id", )