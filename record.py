import man

class Record:
	def __init__(self, title, buyer: man.Man, dateTime=None):
		self.title = title
		self.buyer = buyer
		self.dateTime = dateTime
		self.manDebt = dict()

	@property
	def mans(self):
		mans = set(self.manDebt.keys())
		mans.add(self.buyer)
		return mans

	def __setitem__(self, man: man.Man, amount):
		self.manDebt[man] = amount

	def __getitem__(self, man: man.Man):
		return self.manDebt[man]

	def __contains__(self, man: man.Man):
		mans = self.mans.copy()
		mans.remove(self.buyer)
		if man in mans:
			return True
		return False