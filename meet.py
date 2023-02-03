class Meet:
	def __init__(self, title, records: list, startDate=None, endDate=None):
		self.title = title
		self.records = records
		self.startDate = startDate
		self.endDate = endDate

		self.mans = None
