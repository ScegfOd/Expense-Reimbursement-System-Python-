from selenium.webdriver.support.ui import WebDriverWait

class RequestEIDPage:
	new_request_id = 'newrequest'
	pennies_id = 'pennies'
	reason_id = 'reason'
	reply_id = 'reply0'
	approve_id = 'approve0'
	deny_id = 'deny0'

	def __init__(self, driver):
		self.driver = driver

	def assert_here(self):
		WebDriverWait(self.driver, 5, 1).until(lambda d: 'Reimbursement' in d.page_source)
		assert 'Reimbursement' in self.driver.page_source

	def assert_requests_exist(self):
		WebDriverWait(self.driver, 5, 1).until(lambda d: '<tr>' in d.page_source)
		assert '<tr>' in self.driver.page_source

	def assert_success(self):
		WebDriverWait(self.driver, 5, 1).until(lambda d: 'successful' in d.page_source)
		assert 'successful' in self.driver.page_source

	def click_approve(self):
		WebDriverWait(self.driver, 5, 1).until(lambda d: self.reply_id in d.page_source)
		self.driver.find_element_by_id(self.approve_id).click()

	def click_deny(self):
		WebDriverWait(self.driver, 5, 1).until(lambda d: self.reply_id in d.page_source)
		self.driver.find_element_by_id(self.approve_id).click()

	def click_new_request(self):
		self.driver.find_element_by_id(self.new_request_id).click()

	def enter_an_amount(self):
		self.driver.find_element_by_id(self.pennies_id).send_keys("1337")

	def enter_a_reason(self):
		WebDriverWait(self.driver, 5, 1).until(lambda d: 'reason' in d.page_source)
		self.driver.find_element_by_id(self.reason_id).send_keys("goblins stole my sword")

	def enter_a_reply(self):
		WebDriverWait(self.driver, 5, 1).until(lambda d: self.reply_id in d.page_source)
		self.driver.find_element_by_id(self.reply_id).send_keys("go buy a new sword")
