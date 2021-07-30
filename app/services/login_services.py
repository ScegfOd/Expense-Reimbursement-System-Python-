from app.app import func_call_logger
import app.dao.employee_dao as db
from app.model.employee import Employee

def encrypt(a_password):
	return a_password + '#'

@func_call_logger(__name__)
def get_employee(login_dict):
	an_employee = False
	if 'email' in login_dict and 'password' in login_dict:
		pass_hash = encrypt(str(login_dict['password']))
		email = str(login_dict['email'])
		for employee in db.get_employees():
			someone = Employee(*employee)
			if pass_hash == someone.pass_hash and \
				email == someone.email:
				an_employee = someone.to_dict() # loop through everything
				# 'cause timing attacks
	return an_employee
