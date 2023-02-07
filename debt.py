import record

class Debt(record.Record):
	def __init__(self, title, debtor, creditor, amount, dateTime=None):
		super().__init__(title, creditor, dateTime)
		self.amount = amount
		self.userDebt[debtor] = amount
	
	@property
	def cost(self):
		return 0