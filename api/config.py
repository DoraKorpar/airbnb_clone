import os

env = os.environ.get('AIRBNB_ENV')

if env == 'dev':
	DEBUG = True
	HOST = 'localhost'
	PORT = 3333
	DATABASE = {
		'host': ip
		'user': 'airbnb_user_dev'
		'database': 'airbnb_dev'
		'port': 3306
		'charset': 'utf8'
		'password': os.environ.get('AIRBNB_DATABASE_PWD_DEV')
	}

if env == 'prod':
	DEBUG = False
	HOST = '0.0.0.0'
	PORT = 3000
	DATABASE = {
		'host': ip 
		'user': 'airbnb_user_prod'
		'database': 'airbnb_prod'
		'port': 3306
		'charset': 'utf8'
		'password': os.environ.get('AIRBNB_DATABASE_PWD_PROD')
	}