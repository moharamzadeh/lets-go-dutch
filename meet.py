import record

class Meet:
	def __init__(self, title, startDate=None, endDate=None):
		self.title = title
		self.startDate = startDate
		self.endDate = endDate
		self.records = list()

	def __call__(self, record: record.Record):
		self.records.append(record)

	@property
	def mans(self):
		allMan = set()
		for record in self.records:
			allMan.add(record.buyer)
			allMan.add(record.mans)
		return allMan