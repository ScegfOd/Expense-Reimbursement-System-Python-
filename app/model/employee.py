class Employee:
	def __init__(self, eid = None, email = None, pass_hash = None, is_manager = None):
		self.eid = eid
		self.email = email
		self.pass_hash = pass_hash
		self.is_manager = is_manager == '1'

	def __str__(self):
		return f"ID #{self.eid}, email: '{self.email}'" \
		+ f", password hash: '{self.pass_hash}', manager? {self.is_manager}"

	def to_dict(self):
		return {
			'eid': self.eid,
			'email': self.email,
			'is_manager': self.is_manager
		}

