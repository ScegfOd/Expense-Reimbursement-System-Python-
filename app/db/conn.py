from pyodbc import connect
from app.db.credentials import *

def get_db_connection():
	return connect(f"DRIVER={{PostgreSQL}};SERVER={host};PORT={port};DATABASE={database};UID={username};PWD={password}")
