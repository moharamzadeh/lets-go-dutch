class Meet:
	def __init__(self, title, startDate=None, endDate=None):
		self.title = title
		self.startDate = startDate
		self.endDate = endDate
		self.records = list()
		self.mans = None
