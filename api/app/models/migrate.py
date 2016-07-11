from amenity import Amenity
from city import City
from place import Place
from place_amenities import PlaceAmenities
from place_book import PlaceBook
from state import State
from user import User

database.create_tables([Amenity, City, Place, PlaceAmenities, PlaceBook, State, User])