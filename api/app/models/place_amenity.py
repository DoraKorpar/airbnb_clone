from peewee import *

class PlaceAmenities(peewee.Model):

	place = ForeignKeyField(Place)
	amenity = ForeignKeyField(Amenity)

	class Meta:
		database = database