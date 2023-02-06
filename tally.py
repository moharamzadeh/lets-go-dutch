import meet
import record
import debt
import person
from typing import overload

class Tally:
	def __init__(self, title):
		self.title = title
		self.__meets = list()
		self.__records = list()
		self.__debts = list()

	@overload
	def addData(self, meet: meet.Meet) -> None: ...

	@overload
	def addData(self, debt: debt.Debt) -> None: ...

	@overload
	def addData(self, record: record.Record) -> None: ...

	def addData(self, value) -> None:
		if isinstance(value, meet.Meet):
			return self.__meets.append(value)
		if isinstance(value, debt.Debt):
			return self.__debts.append(value)		
		if isinstance(value, record.Record):
			return self.__records.append(value)
		raise ValueError('You must pass Meet or Record or Debt')

	@property
	def persons(self):
		persons = set()
		for meet in self.__meets:
			persons.update(meet.persons)
		for record in self.__records:
			persons.update(record.persons)
		for debt in self.__debts:
			persons.update(debt.persons)
		return persons

	@property
	def tally(self):
		tally = list()
		for person1 in self.persons:
			for person2 in self.persons:
				def __shartExist(fromPerson, toPerson, listOfDict: list):
					for d in listOfDict:
						if fromPerson is d['from'] and toPerson is d['to']:
							return True
					return False
				if person1 is person2 or __shartExist(person2, person1, tally):
					continue
				hesab = {'from': person1, 'to': person2, 'amount': self.amount(person1, person2), 'status': 'unpaid'}
				tally.append(hesab)
		def toPositiveAmount(listOfDict: list):
			l = listOfDict.copy()
			for d in listOfDict:
				if d['amount'] < 0:
					person1 = d['from']
					person2 = d['to']
					amount = abs(d['amount'])
					l.remove(d)
					hesab = {'from': person2, 'to': person1, 'amount': amount, 'status': 'unpaid'}
					l.append(hesab)
			return l
		tally = toPositiveAmount(tally)
		return tally

	def amount(self, person1: person.Person, person2: person.Person):
		amount = 0
		records = self.records
		for record in records:
			if record.buyer is person2 and person1 in record:
				amount += record.personDebt[person1]
			elif record.buyer is person1 and person2 in record:
				amount -= record.personDebt[person2]
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