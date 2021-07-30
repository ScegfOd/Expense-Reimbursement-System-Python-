Feature: create a reimbursement request

# as an employee, I can create a reimbursement request with an amount and a reason (bonus: file upload)
	@resetdb
	Scenario: An employee is on the request page and wants to make a request
		Given the employee is logged in
		And the user is on the request page
		And the user selects a reason
		And the user enters an amount
		When the user pushes the new request button
		Then the user is given a success message

# as a manager, I can create a reimbursement request with an amount and a reason (bonus: file upload)
	@resetdb
	Scenario: A manager is on the request page and wants to make a request
		Given the manager is logged in
		And the user is on the request page
		And the user selects a reason
		And the user enters an amount
		When the user pushes the new request button
		Then the user is given a success message
