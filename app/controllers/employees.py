from app.app import app, func_call_logger
import app.services.reimbursement_services as rs
from flask import request


# GET for employees to view a single reimbursement request
@app.route("/employees/<int:eid>/reimbursements/<int:rid>", methods = ["GET"])
@func_call_logger(__name__)
def employee_view_reimbursements(eid, rid):
	#TODO employee login?
	if request.method == "GET":
		result = rs.get_reimbursement(rid, eid)
		if result:
			return result, 200
		return "incorrect employee or reimbursement id", 404


# GET for employees to view owned reimbursement requests
# POST for employees to make new reimbursement requests
@app.route("/employees/<int:eid>/reimbursements", methods = ["GET", "POST"])
@func_call_logger(__name__)
def reimbursements_for(eid):
	#TODO employee login?
	if request.method == "GET":
		result = rs.get_all_reimbursements(eid)
		if result:
			return result, 200
		return f"no reimbursement requests found for employee #{eid}", 404

	if request.method == "POST":
		if rs.post_reimbursements(eid, request.get_json()):
			return "new request submitted!", 201
		return "invalid id or request", 400


