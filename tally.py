import meet
import record
import debt
import man

class Tally:
	def __init__(self, title):
		self.title = title
		self.__meets = list()
		self.__records = list()
		self.__debts = list()

	def __setitem__(self, type: str, value):
		if type == 'meet':
			self.__meets.append(value)
		elif type == 'record':
			self.__records.append(value)
		elif type == 'debt':
			self.__debts.append(value)

	@property
	def tally(self):
		pass

	@property
	def records(self):
		records = list()
		records.extend(self.__debts)
		records.extend(self.__records)
		for meet in self.__meets:
			records.extend(meet.records)
		return records