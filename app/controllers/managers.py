from app.app import app, func_call_logger
from flask import request
import app.services.reimbursement_services as rs
import app.services.stats_services as ss


# GET for managers to view all reimbursement requests
@app.route("/managers/<int:mid>/reimbursements", methods = ["GET"])
@func_call_logger(__name__)
def all_reimbursements(mid):
	#TODO 401 if not logged in or employee login
	full_list = rs.get_all_reimbursements()
	if full_list:
		return full_list, 200
	return "no reimbursements found", 404


# GET for managers to view reimbursement requests
# POST for managers to approve/disapprove of reimbursement requests
@app.route("/managers/<int:mid>/reimbursements/<int:rid>", methods = ["GET", "PUT"])
@func_call_logger(__name__)
def managers_view_reimbursement(mid, rid):
	#TODO 401 if not logged in or employee login
	if request.method == "GET":
		result = rs.get_reimbursement(rid)
		if result:
			return result, 200
		return "reimbursement not found", 404

	if request.method == "PUT":
		result = rs.put_reimbursements(mid, rid, request.get_json())
		if result:
			return "reimbursement request updated", 200
		return "can't update that reimbursement request", 404


# GET for managers to view reimbursement requests by employee
@app.route("/managers/<int:mid>/reimbursements/employees/<int:eid>", methods = ["GET"])
@func_call_logger(__name__)
def manager_view_reimbursements_for(mid, eid):
	#TODO 401 if not logged in or employee login
	if request.method == "GET":
		result = rs.get_all_reimbursements(eid)
		if result:
			return result, 200
		return f"no reimbursement requests found for employee #{eid}", 404


# GET for managers to view reimbursement requests
@app.route("/managers/<int:mid>/reimbursements/statistics", methods = ["GET"])
@func_call_logger(__name__)
def reimbursement_statistics(mid):
	#TODO 401 if not logged in or employee login
	result = ss.get_stats()
	if result:
		return result, 200
	return "no requests to show stats for", 200


