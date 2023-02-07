import record

class Meet:
	def __init__(self, title, startDate=None, endDate=None):
		self.title = title
		self.startDate = startDate
		self.endDate = endDate
		self.records = list()

	def addRecord(self, *records: record.Record):
		for record in records:
			self.records.append(record)

	@property
	def cost(self):
		cost = 0
		for record in self.records:
			cost += record.cost
		return cost

	@property
	def persons(self):
		persons = set()
		persons.update(self.buyers)
		persons.update(self.users)
		return persons

	@property
	def users(self):
		users = set()
		for record in self.records:
			users.update(record.users)
		return users

	@property
	def buyers(self):
		buyers = set()
		for record in self.records:
			buyers.add(record.buyer)
		return buyers