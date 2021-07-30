class Request:
	def __init__(self,
			response_id = None,
			owner_id    = None,
			pennies     = None,
			reason      = None,
			is_pending  = None,
			response    = None,
			is_approved = None):
		self.rid         = response_id
		self.eid         = owner_id
		self.pennies     = pennies
		self.reason      = reason
		self.is_pending  = is_pending == "1"
		self.response    = response
		self.is_approved = is_approved == "1"

	def __str__(self):
		return f"ID #{self.rid}" +\
		f"\nrequestor ID #{self.eid}" +\
		f"\npennies requested: {self.pennies}" +\
		f"\npending: {self.is_pending}" +\
		f"\napproved: {self.is_approved}" +\
		f"\nreason given: '{self.reason}'" +\
		f"\nresponse: '{self.response}'"

	def to_dict(self):
		return {
			"rid"         : self.rid,
			"eid"         : self.eid,
			"pennies"     : self.pennies,
			"reason"      : self.reason,
			"is_pending"  : self.is_pending,
			"response"    : self.response,
			"is_apprived" : self.is_approved,
		}

