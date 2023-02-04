import meet
import record
import debt
import man

class Tally:
	def __init__(self, title):
		self.title = title
		self.meets = list()
		self.records = list()
		self.debts = list()

	def __setitem__(self, type: str, value):
		if type == 'meet':
			self.meets.append(value)
		elif type == 'record':
			self.records.append(value)
		elif type == 'debt':
			self.__debts.append(value)

	@property
	def tally(self):
		pass