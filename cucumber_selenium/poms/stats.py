from selenium.webdriver.support.ui import WebDriverWait

class StatsPage:

	def __init__(self, driver):
		self.driver = driver

	def assert_here(self):
		WebDriverWait(self.driver, 5, 1).until(lambda d: 'Statistics' in d.page_source)
		assert 'Statistics' in self.driver.page_source

	def assert_stats_exist(self):
		WebDriverWait(self.driver, 5, 1).until(lambda d: "request" in d.page_source)
		assert "request" in self.driver.page_source

	def click_stats(self):
		self.assert_here()
		self.driver.find_elements_by_xpath('//p[contains(text(), "Statistics")]')[0].click()

