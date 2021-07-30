import unittest
from unittest.mock import Mock
from db_init.pyreset import resetdb
import app.dao.employee_dao as test

# there isn't really anything to test in the DAO except that the SQL query was
#  written correctly, but DAO tests are required so I'll do my best...
class employee_dao_test(unittest.TestCase):
	def setUp(self):
		resetdb()

	def test_get_all_employees(self):
		self.assertEqual(5,len(test.get_employees()))

	def test_get_all_employees(self):
		self.assertEqual(1,len(test.get_employees_by_eid(4)))

	@classmethod
	def tearDownClass(cls):
		resetdb()
