from app.dao.dao_boiler_plate import logs_and_db_connection


@logs_and_db_connection(__name__)
def avg_pennies_requests(db):
	db.execute("SELECT avg(pennies) FROM requests")
	return db.fetchall()


@logs_and_db_connection(__name__)
def avg_pennies_requests_for_eid(db, eid):
	db.execute("SELECT avg(pennies) FROM requests WHERE eid = ?", eid)
	return db.fetchall()


@logs_and_db_connection(__name__)
def get_requests(db):
	db.execute("SELECT * FROM requests")
	return db.fetchall()


@logs_and_db_connection(__name__)
def get_requests_by_eid(db, eid):
	db.execute("""SELECT * FROM requests WHERE
		eid = ?""",
		eid)
	return db.fetchall()


@logs_and_db_connection(__name__)
def get_requests_id(db, rid):
	db.execute("""SELECT * FROM requests WHERE
		id = ?""",
		rid)
	return db.fetchall()


@logs_and_db_connection(__name__)
def get_max_spender_eid(db):
	db.execute("""SELECT eid FROM (
			SELECT eid, sum(pennies) AS maxes FROM requests GROUP BY eid
		) AS foo WHERE maxes = (
			SELECT max(maxes) from (
				SELECT eid, sum(pennies) AS maxes FROM requests GROUP BY eid
			) AS bar
		)""")
	return db.fetchall()


@logs_and_db_connection(__name__)
def max_pennies_requests(db):
	db.execute("SELECT max(pennies) FROM requests")
	return db.fetchall()


@logs_and_db_connection(__name__)
def post_requests_eid(db, eid, pennies, reason = "DEFAULT"):
	db.execute("""INSERT INTO requests VALUES
		(DEFAULT, ?, ?, ?, DEFAULT, NULL, DEFAULT)""",
		eid,
		pennies,
		reason)
	db.commit()
	return True


@logs_and_db_connection(__name__)
def put_requests(db, rid, pennies, reason, is_pending, response, is_approved):
	db.execute("""UPDATE requests SET
		pennies = ?,
		reason = ?,
		is_pending = ?,
		response = ?,
		is_approved = ?
		WHERE id = ?""",
		pennies,
		reason,
		is_pending,
		response,
		is_approved,
		rid)
	db.commit()
	return True
