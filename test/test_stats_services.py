import unittest
from unittest.mock import Mock
import app.services.stats_services as test
import app.dao.employee_dao as edb
import app.dao.request_dao as rdb
from app.model.employee import Employee
from app.model.request import Request

class stats_services_test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.get_employees_by_eid = edb.get_employees_by_eid
		edb.get_employees_by_eid = Mock(return_value=[(
				4,
				'email@place.com',
				'passhash#',
				True,
			)])

		cls.avg_pennies_requests = rdb.avg_pennies_requests
		rdb.avg_pennies_requests = Mock(return_value=[
				(500,)
			])
		cls.avg_pennies_requests_for_eid = rdb.avg_pennies_requests_for_eid
		rdb.avg_pennies_requests_for_eid = Mock(side_effect = lambda x : [[x*1000]])
		cls.get_max_spender_eid = rdb.get_max_spender_eid
		rdb.get_max_spender_eid = Mock(return_value=[
				(4,)
			])
		cls.get_requests = rdb.get_requests
		cls.max_pennies_requests = rdb.max_pennies_requests
		rdb.max_pennies_requests = Mock(return_value=[
				(9001,)
			])

	def test_get_max_pennies_request(self):
		self.assertEqual(type(Request()),type(test.get_max_pennies_request()))

	def test_get_max_spender(self):
		self.assertEqual(type(Employee()),type(test.get_max_spender()))
		self.assertEqual(4,test.get_max_spender().eid)

	def test_get_mean_pennies(self):
		self.assertEqual(500,test.get_mean_pennies())
		self.assertEqual(4000,test.get_mean_pennies(4))

	def test_get_stats(self):
		rdb.get_requests = Mock(return_value=[[]])
		self.assertFalse(test.get_stats())
		rdb.get_requests = Mock(return_value=[
			('request tuple #1'),
			('request tuple #2'),
		])
		self.assertEquals(type(dict()),type(test.get_stats()))

	@classmethod
	def tearDownClass(cls):
		edb.get_employees_by_eid = cls.get_employees_by_eid

		rdb.avg_pennies_requests = cls.avg_pennies_requests
		rdb.avg_pennies_requests_for_eid = cls.avg_pennies_requests_for_eid
		rdb.get_max_spender_eid = cls.get_max_spender_eid
		rdb.get_requests = cls.get_requests
		rdb.max_pennies_requests = cls.max_pennies_requests
