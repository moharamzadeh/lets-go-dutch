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
	def mans(self):
		mans = set()
		for meet in self.__meets:
			mans.update(meet.mans)
		for record in self.__records:
			mans.update(record.mans)
		for debt in self.__debts:
			mans.update(debt.mans)
		return mans

	@property
	def tally(self):
		tally = list()
		for man1 in self.mans:
			for man2 in self.mans:
				def __shartExist(fromMan, toMan, listOfDict: list):
					for d in listOfDict:
						if fromMan is d['from'] and toMan is d['to']:
							return True
					return False
				if man1 is man2 or __shartExist(man2, man1, tally):
					continue
				hesab = {'from': man1, 'to': man2, 'amount': self.amount(man1, man2), 'status': 'unpaid'}
				tally.append(hesab)
		def toPositiveAmount(listOfDict: list):
			l = listOfDict.copy()
			for d in listOfDict:
				if d['amount'] < 0:
					man1 = d['from']
					man2 = d['to']
					amount = abs(d['amount'])
					l.remove(d)
					hesab = {'from': man2, 'to': man1, 'amount': amount, 'status': 'unpaid'}
					l.append(hesab)
			return l
		tally = toPositiveAmount(tally)
		return tally

	def amount(self, man1: man.Man, man2: man.Man):
		amount = 0
		records = self.records
		for record in records:
			if record.buyer is man2 and man1 in record:
				amount += record.manDebt[man1]
			elif record.buyer is man1 and man2 in record:
				amount -= record.manDebt[man2]
		return amount

	@property
	def records(self):
		records = list()
		records.extend(self.__debts)
		records.extend(self.__records)
		for meet in self.__meets:
			records.extend(meet.records)
		return records

	def __repr__(self):
		result = ''
		for d in self.tally:
			result += f"{str(d['from'])} to {str(d['to'])}: {d['amount']}\n"
		return result