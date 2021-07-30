from app.app import func_call_logger
import app.dao.request_dao as db
from app.model.request import Request


@func_call_logger(__name__)
def get_reimbursement(rid, eid = -1): # -1 for managers
	result = None
	for a_tuple in db.get_requests_id(rid):
		result = Request(*a_tuple) #should be exactly zero or one matching request

	if result:
		# eid not required for managers, they can view any reimbursement request
		if -1 == eid or result.eid == eid:
			return {result.rid : result.to_dict()}
	return False


@func_call_logger(__name__)
def get_all_reimbursements(eid = -1): # -1 for managers viewing all reimbursements
	if eid != -1:
		tuple_list = db.get_requests_by_eid(eid)
	else:
		tuple_list = db.get_requests()

	result = dict()
	for a_tuple in tuple_list:
		an_object = Request(*a_tuple)
		result[an_object.rid] = an_object.to_dict()
	if len(result):
		return result
	return False


@func_call_logger(__name__)
def post_reimbursements(eid, request_json = None):
	if not request_json:
		request_json = dict()

	reason = request_json.get('reason', None)
	pennies = request_json.get('pennies', 0) # zero pennies are allowed!
	if reason != None or pennies != 0:
		return db.post_requests_eid(eid, pennies, reason)
	return False


@func_call_logger(__name__)
def put_reimbursements(mid, rid, request_json = None):
	request = None
	for a_tuple in db.get_requests_id(rid):
		request = Request(*a_tuple) #should be exactly zero or one matching request
	if not request:
		# you can't approve a non-existant request
		return False

	if not request_json:
		request_json = dict()
	response = request_json.get('response', None)
	is_approved = request_json.get('is_approved', False)

	if request.eid == mid and is_approved:
		# also, you can't approve your own request
		response = 'castigate the manager approving his own request'
		is_approved = False

	return db.put_requests(rid, request.pennies, request.reason, False, response, is_approved)
