# as a manager, I can view a 'statistics' page. This page includes information like what employee spends the most money, mean expenditure cost etc...
Feature: manager can view a statistics page for various reimbursement request statistics
	Background:
		Given the manager is logged in

	Scenario: A manager wants to see the statistics page
		And the manager clicks the statistics page in the nav bar
		Then the statistics page shows up
		And it shows which employee spends the most money
		And it shows the mean value of all reimbursement request amounts
