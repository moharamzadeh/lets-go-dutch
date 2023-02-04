import record

class Debt(record.Record):
	def __init__(self, title, debtor, creditor, amount, dateTime=None):
		self.title = title
		self.buyer = debtor
		self.dateTime = dateTime
		self.manDebt = dict()
		self.manDebt[creditor] = amount

	def __setitem__(self):
		pass