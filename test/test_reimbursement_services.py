import unittest
from unittest.mock import Mock
import app.services.reimbursement_services as test
import app.dao.request_dao as db

class login_service_test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.requests = [
			(1, 1, 420, 'dank memes', True, None, False),
			(2, 6, 1337, '$13.37 for the memes', True, None, False),
			(3, 2, 10000, 'hundred dollar meal with client', False, '10k pennies 4 u', True),
			(4, 3, 100, 'pay me back', False, 'no dollar for you', False),
			(5, 3, 100, 'pay me back', False, 'no dollar for you', False),
		]
		cls.put_requests = db.put_requests
		cls.post_requests_eid = db.post_requests_eid
		cls.get_requests_id = db.get_requests_id
		cls.get_requests = db.get_requests
		cls.get_requests_by_eid = db.get_requests_by_eid
		db.get_requests_id = Mock(side_effect = lambda x : [ row for row in cls.requests if row[0] == x ])
		db.get_requests = Mock(return_value = cls.requests)
		db.get_requests_by_eid = Mock(side_effect =lambda x : [ row for row in cls.requests if row[1] == x ])
		# can't use a lambda wrapping our data if we want to persist changes:
		db.post_requests_eid = Mock(side_effect = cls.append_requests)
		db.put_requests = Mock(side_effect = cls.update_requests)

	@classmethod
	def append_requests(cls, eid, pennies, reason):
		cls.requests.append(
		(
			len(cls.requests),
			eid,
			pennies,
			'dank memes',
			True,
			None,
			False)
		)

	@classmethod
	def update_requests(cls, rid, pennies, reason, is_pending, response, is_approved):
		cls.requests[rid-1] = (
			rid,
			cls.requests[rid][1],
			pennies,
			reason,
			is_pending,
			response,
			is_approved,
		)
		return not (is_pending and is_approved)

	def test_get_reimbursement(self):
		self.assertEqual(type(dict()),type(test.get_reimbursement(1)))
		self.assertEqual(type(dict()),type(test.get_reimbursement(2)))
		self.assertEqual(False,test.get_reimbursement(6))
		self.assertEqual(type(dict()),type(test.get_reimbursement(2,6)))
		self.assertEqual(False,test.get_reimbursement(2,1))


	def test_get_all_reimbursements(self):
		self.assertEqual(1,len(test.get_all_reimbursements(1)))
		self.assertEqual(1,len(test.get_all_reimbursements(2)))
		self.assertEqual(False,test.get_all_reimbursements(5))
		self.assertEqual(2,len(test.get_all_reimbursements(3)))
		self.assertEqual(5,len(test.get_all_reimbursements()))


	def test_post_reimbursements(self):
		self.assertEqual(None,test.post_reimbursements(1, { 'pennies': 100, 'reason': 'need a $' }))
		self.assertEqual(6,len(self.requests))
		self.assertEqual(None,test.post_reimbursements(1, { 'pennies': 999 }))
		self.assertEqual(None,test.post_reimbursements(1, { 'reason': "not technically a reimbursement" }))
		self.assertEqual(False,test.post_reimbursements(1, {}))
		self.assertEqual(False,test.post_reimbursements(1))
		self.assertEqual(8,len(self.requests))
		del self.requests[-1]
		del self.requests[-1]
		del self.requests[-1]


	def test_put_reimbursements(self):
		self.assertEqual(False,test.put_reimbursements(1, 9001, { 'response': 'go away', 'is_approved': False }))
		self.assertEqual(True,test.put_reimbursements(6, 2, { 'response': 'sigh, oops', 'is_approved': False }))
		self.assertEqual('sigh, oops', self.requests[2-1][-2])
		self.assertEqual(True,test.put_reimbursements(1, 1, { 'response': 'go away', 'is_approved': True }))
		self.assertEqual('castigate the manager approving his own request', self.requests[1-1][-2])
		self.assertEqual(True,test.put_reimbursements(1, 3, { 'response': 'go away', 'is_approved': False }))
		db.put_requests = Mock(return_value = None) # db (database) broke between calls
		self.assertEqual(None,test.put_reimbursements(1, 4, { 'response': 'go away', 'is_approved': False }))
		db.put_requests = Mock(side_effect = self.update_requests) #intermittent db issues
		self.assertEqual(True,test.put_reimbursements(1, 4, { 'response': 'go away', 'is_approved': False }))
		self.assertEqual(True,test.put_reimbursements(1, 4, { 'is_approved': False }))
		self.assertEqual(True,test.put_reimbursements(1, 4, { 'response': 'go away' }))
		self.assertEqual(True,test.put_reimbursements(1, 4, {}))
		self.assertEqual(True,test.put_reimbursements(1, 4, None))


	@classmethod
	def tearDownClass(cls):
		db.get_requests_id = cls.get_requests_id
		db.get_requests = cls.get_requests
		db.get_requests_by_eid = cls.get_requests_by_eid
		db.post_requests_eid = cls.post_requests_eid
		db.put_requests = cls.put_requests
