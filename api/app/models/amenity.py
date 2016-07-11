from peewee import *
from base import BaseModel

class Amenity(BaseModel):
	name = CharField(128, null=False)