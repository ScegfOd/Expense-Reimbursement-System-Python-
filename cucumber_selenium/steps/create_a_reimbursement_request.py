
######################################################################
#these tests auto generated with svw.py (salt, vinegar, & water) -JJC#
######################################################################

from behave import *

@given("the employee is logged in")
def step_the_employee_is_logged_in(context):
	context.driver.get(context.index)
	context.pg_login.login_employee()


@given("the user is on the request page")
def step_the_user_is_on_the_request_page(context):
	context.pg_request_eid.assert_here()


@when("the user pushes the new request button")
def step_the_user_pushes_the_new_request_button(context):
	context.pg_request_eid.click_new_request()


@given("the user selects a reason")
def step_the_user_selects_a_reason(context):
	context.pg_request_eid.enter_a_reason()


@given("the user enters an amount")
def step_the_user_enters_an_amount(context):
	context.pg_request_eid.enter_an_amount()


@then("the user is given a success message")
def step_the_user_is_given_a_success_message(context):
	context.pg_request_eid.assert_success()

