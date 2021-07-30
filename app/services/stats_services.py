from app.app import func_call_logger
import app.dao.request_dao as rdb
import app.dao.employee_dao as edb
from app.services.reimbursement_services import get_all_reimbursements
from app.model.employee import Employee
from app.model.request import Request


@func_call_logger(__name__)
def get_max_pennies_request():
	return Request(*(rdb.max_pennies_requests()[0])) # just one row in table returned


@func_call_logger(__name__)
def get_max_spender():
	eid = rdb.get_max_spender_eid()[0][0] # just one entry in table returned
	max_spender = None
	for a_tuple in edb.get_employees_by_eid(eid):
		max_spender = Employee(*a_tuple)
	return max_spender


@func_call_logger(__name__)
def get_mean_pennies(eid = -1):
	if eid == -1:
		return rdb.avg_pennies_requests()[0][0]
	return rdb.avg_pennies_requests_for_eid(eid)[0][0]


@func_call_logger(__name__)
def get_stats():
	if len(rdb.get_requests()[0]):
		result = dict()
		max_spender = get_max_spender()
		result['max_spend_employee'] = max_spender.to_dict()
		result['max_spend_employee_all_request'] = get_all_reimbursements(max_spender.eid)
		result['max_spend_employee_max_request'] = max(result['max_spend_employee_all_request'].values(),
			key=lambda x : x['pennies'])
		result['max_spend_employee_mean_request'] = int(get_mean_pennies(max_spender.eid))
		result['all_request_mean_request'] = int(get_mean_pennies())
		result['all_request_max_request'] = get_max_pennies_request().to_dict()
		return result
	return False


