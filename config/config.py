import os
import MySQLdb

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

APP_NAME = 'Falcon'

def dbsetup():
	db = MySQLdb.connect("localhost","root","root","falconDB" )
	return db
