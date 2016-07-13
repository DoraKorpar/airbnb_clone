# imports app object from __init__ file in app directory
from app import app, json

import sys
sys.path.append("..")
from config import *

# run app, passing settings imported from config file
if __name__ == '__main__':
	app.run(host=HOST, port=PORT, debug=DEBUG)