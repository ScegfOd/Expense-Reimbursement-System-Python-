Feature: app login
	Background: A user is on the login page and wants to log in
		Given the user is on the login page

# as an employee, I can log in to access employee portions of the app
# as an employee, I can view reimbursement requests I have made previously whether pending, approved, or denied
	Scenario: An employee would like to log in
		Given the employee enters the correct email
		And the employee enters the correct password
		When the user pushes the submit button
		Then the user is redirected to the request page and requests are shown

# as a manager, I can log in to access manager portions of the app
# as a manager, I can view any/all reimbursement requests whether pending, approved, or denied
	Scenario: A manager would like to log in
		Given the manager enters the correct email
		And the manager enters the correct password
		When the user pushes the submit button
		Then the user is redirected to the request page and requests are shown
