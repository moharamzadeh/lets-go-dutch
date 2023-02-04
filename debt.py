import record

class Debt(record.Record):
	def __init__(self, title, debtor, creditor, amount, dateTime=None):
		self.title = title
		self.buyer = creditor
		self.dateTime = dateTime
		self.manDebt = dict()
		self.manDebt[debtor] = amount

	def __setitem__(self):
		pass