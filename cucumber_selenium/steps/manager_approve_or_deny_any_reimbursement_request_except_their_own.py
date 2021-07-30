
######################################################################
#these tests auto generated with svw.py (salt, vinegar, & water) -JJC#
######################################################################

from behave import *

#Scenario #1: A manager is on the request page and wants deny another's previously made request

@when("the manager clicks the denied button")
def blah(context):
	context.pg_request_eid.click_deny()

@then("the page shows that the request was denied")
def blah(context):
	context.pg_request_eid.assert_success()

#Scenario #2: A manager is on the request page and wants approve another's previously made request

@when("the manager clicks the approve button")
def blah(context):
	context.pg_request_eid.click_approve()

@then("the page shows that the request was approved")
def blah(context):
	context.pg_request_eid.assert_success()

#Scenario #3: A manager is on the request page and wants approve another's previously made request with a message

@when("the manager enters a reason")
def step_the_manager_enters_a_reason(context):
	context.pg_request_eid.enter_a_reply()

