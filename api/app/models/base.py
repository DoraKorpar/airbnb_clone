import peewee
import datetime
from ....config import *

database = peewee.MySQLDatabase(DATABASE)

class BaseModel(peewee.Model):
	id = peewee.PrimaryKeyField(unique=True)
	created_at = peewee.DateTimeField(default=datetime.datetime.now())
	updated_at = peewee.DateTimeField(default=datetime.datetime.now())

	def save(self, *args, **kwargs):
		self.updated_at = datetime.datetime.now()
		return super(BaseModel, self).save(*args, **kwargs)

	class Meta:
		database = database
		order_by = ("id", )