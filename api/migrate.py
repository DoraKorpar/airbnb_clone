from amenity import Amenity
from models.city import City
from models.place import Place
from models.place_amenities import PlaceAmenities
from models.place_book import PlaceBook
from models.state import State
from models.user import User
from app.models.base import database

# generates every table in the database
database.create_tables([
	Amenity, 
	City, 
	Place, 
	PlaceAmenities, 
	PlaceBook, 
	State, 
	User])