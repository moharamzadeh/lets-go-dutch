import record

class Debt(record.Record):
	def __init__(self, title, debtor, creditor, amount, dateTime=None):
		super().__init__(title, creditor, dateTime)
		self.userDebt[debtor] = amount