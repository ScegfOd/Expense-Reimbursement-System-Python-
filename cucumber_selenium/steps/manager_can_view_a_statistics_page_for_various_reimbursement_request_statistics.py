
######################################################################
#these tests auto generated with svw.py (salt, vinegar, & water) -JJC#
######################################################################

from behave import *

#Background: d:

@given("the manager is logged in")
def step_the_manager_is_logged_in(context):
	context.driver.get(context.index)
	context.pg_login.login_manager()


#Scenario #1: A manager wants to see the statistics page

@given("the manager clicks the statistics page in the nav bar")
def step_the_manager_clicks_the_statistics_page_in_the_nav_bar(context):
	context.pg_stats.click_stats()


@then("the statistics page shows up")
def step_the_statistics_page_shows_up(context):
	context.pg_stats.assert_here()


@then("it shows which employee spends the most money")
def step_it_shows_which_employee_spends_the_most_money(context):
	context.pg_stats.assert_stats_exist()


@then("it shows the mean value of all reimbursement request amounts")
def step_it_shows_the_mean_value_of_all_reimbursement_request_amounts(context):
	context.pg_stats.assert_stats_exist()

