from peewee import *
from base import BaseModel

class State(BaseModel):
	name = CharField(128, null=False, unique=True)