from selenium import webdriver
from subprocess import call
from poms.login import LoginPage
from poms.request_eid import RequestEIDPage
from poms.stats import StatsPage


def resetdb():
	call("cd ../db_init && ./reset.sh", shell=True)

def before_all(context):
	context.driver = webdriver.Firefox() # the one true browser
	context.pg_login = LoginPage(context.driver)
	context.pg_request_eid = RequestEIDPage(context.driver)
	context.pg_stats = StatsPage(context.driver)
	context.index = 'http://localhost:5000/static/index.html'

def before_step(context, step):
	pass

def before_scenario(context, scenario):
	pass

def before_feature(context, feature):
	pass

def before_tag(context, tag):
	pass

def after_tag(context, tag):
	if tag == 'resetdb':
		resetdb()

def after_feature(context, feature):
	pass

def after_scenario(context, scenario):
	pass

def after_step(context, step):
	pass

def after_all(context):
	context.driver.quit()
	resetdb()
