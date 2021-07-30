import unittest
from unittest.mock import Mock
from db_init.pyreset import resetdb
import app.dao.request_dao as test

# there isn't really anything to test in the DAO except that the SQL query was
#  written correctly, but DAO tests are required so I'll do my best...
class request_dao_test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		resetdb()

	def test_avg_pennies_requests(self):
		self.assertEqual(1952, int(test.avg_pennies_requests()[0][0]))

	def test_avg_pennies_requests_for_eid(self):
		self.assertEqual(1000, int(test.avg_pennies_requests_for_eid(4)[0][0]))

	def test_get_all(self):
		self.assertEqual(17,len(test.get_requests()))

	def test_get_by_rid(self):
		self.assertEqual(1,len(test.get_requests_id(1)))
		self.assertEqual(0,len(test.get_requests_id(-1)))

	def test_get_by_eid(self):
		self.assertEqual(2,len(test.get_requests_by_eid(6)))
		self.assertEqual(1,len(test.get_requests_by_eid(1)))
		self.assertEqual(0,len(test.get_requests_by_eid(-1)))

	def test_get_max_spender_eid(self):
		self.assertEqual(4,test.get_max_spender_eid()[0][0])

	def test_max_pennies_requests(self):
		self.assertEqual(10000, int(test.max_pennies_requests()[0][0]))

	def test_post_requests_eid(self):
		self.assertEqual(11,len(test.get_requests_by_eid(4)))
		self.assertEqual(True,test.post_requests_eid(4,100))
		self.assertEqual(12,len(test.get_requests_by_eid(4)))

	def test_put_requests(self):
		#pennies, reason, is_pending, response, is_approved
		stuff = (50, 'stuff', False, 'no stuff 4 u', False)
		bad_stuff = (50, 'stuff', True, 'updated stuff!', True)
		self.assertEqual(True, test.put_requests(5, *stuff))
		self.assertEqual(None, test.put_requests(5, *bad_stuff))
		self.assertEqual('no stuff 4 u', test.get_requests_id(5)[0][-2])

	@classmethod
	def tearDownClass(cls):
		resetdb()
