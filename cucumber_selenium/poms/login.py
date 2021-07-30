class LoginPage:
	email_id = 'email'
	password_id = 'password'
	submit_id = 'submit'

	def __init__(self, driver):
		self.driver = driver

	def assert_here(self):
		assert '<header><h1>Login</h1></header>' in self.driver.page_source

	def enter_manager_email(self):
		self.driver.find_element_by_id(self.email_id).send_keys('Tim@lol.com')

	def enter_manager_password(self):
		self.driver.find_element_by_id(self.password_id).send_keys('TtE')

	def enter_employee_email(self):
		self.driver.find_element_by_id(self.email_id).send_keys('BobJim@lol.com')

	def enter_employee_password(self):
		self.driver.find_element_by_id(self.password_id).send_keys('imwithjim')

	def click_login_button(self):
		self.driver.find_element_by_id(self.submit_id).click()

	def login_employee(self):
		self.assert_here()
		self.enter_employee_email()
		self.enter_employee_password()
		self.click_login_button()

	def login_manager(self):
		self.assert_here()
		self.enter_manager_email()
		self.enter_manager_password()
		self.click_login_button()
