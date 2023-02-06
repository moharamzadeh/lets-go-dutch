import record

class Meet:
	def __init__(self, title, startDate=None, endDate=None):
		self.title = title
		self.startDate = startDate
		self.endDate = endDate
		self.records = list()

	def __call__(self, *record: record.Record):
		for r in record:
			self.records.append(r)

	@property
	def persons(self):
		allPerson = set()
		for record in self.records:
			allPerson.add(record.buyer)
			allPerson.update(record.persons)
		return allPerson