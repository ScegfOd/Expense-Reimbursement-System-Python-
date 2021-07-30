# as a manager, I can approve or deny any (except their own) pending request (optionally leaving a message)
Feature: manager approve or deny any reimbursement request except their own
	Background:
		Given the manager is logged in

	@resetdb
	Scenario: A manager is on the request page and wants deny another's previously made request
		When the manager clicks the denied button
		Then the page shows that the request was denied

	@resetdb
	Scenario: A manager is on the request page and wants approve another's previously made request
		When the manager clicks the approve button
		Then the page shows that the request was approved

	@resetdb
	Scenario: A manager is on the request page and wants approve another's previously made request with a message
		When the manager enters a reason
		When the manager clicks the approve button
		Then the page shows that the request was approved
