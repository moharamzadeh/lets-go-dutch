import man

class Record:
	def __init__(self, title, buyer: man.Man, dateTime=None):
		self.title = title
		self.buyer = buyer
		self.dateTime = dateTime
		self.status = 'unpaid'
		self.manDebt = dict()

	def __setitem__(self, man: man.Man, amount):
		self.manDebt[man] = amount

	def __call__(self, status: str):
		self.status = status

	def __bool__(self):
		if self.status == 'paid':
			return True
		return False