import unittest
from unittest.mock import Mock
import app.services.login_services as test
import app.dao.employee_dao as db
from app.model.employee import Employee

class login_service_test(unittest.TestCase):
	def setUp(self):
		db.get_all_employees = Mock(return_value=[
				(1, 'Tim@lol.com', 'TtE#', True),
				(2, 'Slim@lol.com','phat#', False),
				(3, 'JimBob@lol.com','imwithbob#', False),
				(4, 'BobJim@lol.com','imwithjim#', False),
				(6, 'JC@lol.com','selfinsert#', True),
			])

	def test_wrong_credentials(self):
		wrong_credentials = {'email': 'fail@notlol.com', 'password': 'drowssap'}
		self.assertEqual(False,test.get_employee(wrong_credentials))

	def test_wrong_password(self):
		wrong_password = {'email': 'Slim@lol.com', 'password': 'fat'}
		self.assertEqual(False,test.get_employee(wrong_password))

	def test_wrong_email(self):
		wrong_email = {'email': 'milS@lol.com', 'password': 'phat'}
		self.assertEqual(False,test.get_employee(wrong_email))

	def test_correct_credentials(self):
		correct_credentials = {'email': 'Slim@lol.com', 'password': 'phat'}
		self.assertEqual(type(dict()), type(test.get_employee(correct_credentials)))
