import record

class Debt(record.Record):
	def __init__(self, title, debtor, creditor, amount, dateTime=None):
		self.title = title
		self.buyer = creditor
		self.dateTime = dateTime
		self.userDebt = dict()
		self.userDebt[debtor] = amount