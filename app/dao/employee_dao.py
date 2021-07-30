from app.dao.dao_boiler_plate import logs_and_db_connection


@logs_and_db_connection(__name__)
def get_employees(db):
	db.execute("SELECT * FROM employees")
	return db.fetchall()


@logs_and_db_connection(__name__)
def get_employees_by_eid(db, eid):
	db.execute("SELECT * FROM employees WHERE id = ?", eid)
	return db.fetchall()
