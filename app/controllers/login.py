from app.app import app, func_call_logger
from app.services.login_services import get_employee
from flask import request

@app.route("/login", methods = ["POST"])
@func_call_logger(__name__)
def login():
	employee_dict = get_employee(request.get_json())
	if employee_dict:
		return employee_dict, 200
	else:
		return "incorrect email or password", 401
