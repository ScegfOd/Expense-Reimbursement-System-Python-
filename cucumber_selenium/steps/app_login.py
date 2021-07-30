
######################################################################
#these tests auto generated with svw.py (salt, vinegar, & water) -JJC#
######################################################################

from behave import *

#Background: d: A user is on the home page and wants to log in

@given("the user is on the login page")
def step_the_user_is_on_the_home_page(context):
	context.driver.get(context.index)
	context.pg_login.assert_here()


#Scenario #1: An employee would like to log in

@given("the employee enters the correct email")
def step_the_employee_enters_the_correct_email(context):
	context.pg_login.enter_employee_email()


@given("the employee enters the correct password")
def step_the_employee_enters_the_correct_password(context):
	context.pg_login.enter_employee_password()


@when("the user pushes the submit button")
def step_the_user_pushes_the_submit_button(context):
	context.pg_login.click_login_button()


@then("the user is redirected to the request page and requests are shown")
def step_the_user_is_redirected_to_the_request_page(context):
	context.pg_request_eid.assert_here()
	context.pg_request_eid.assert_requests_exist()


#Scenario #2: A manager would like to log in

@given("the manager enters the correct email")
def step_the_manager_enters_the_correct_email(context):
	context.pg_login.enter_manager_email()


@given("the manager enters the correct password")
def step_the_manager_enters_the_correct_password(context):
	context.pg_login.enter_manager_password()

