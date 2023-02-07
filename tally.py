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
		persons.update(self.buyers)
		persons.update(self.users)
		return persons

	@property
	def users(self):
		users = set()
		for meet in self.__meets:
			users.update(meet.users)
		for record in self.__records:
			users.update(record.users)
		return users

	@property
	def buyers(self):
		buyers = set()
		for meet in self.__meets:
			buyers.update(meet.buyers)
		for record in self.__records:
			buyers.add(record.buyer)
		return buyers

	@property
	def tallyList(self):
		tallyList = list()
		for person1 in self.persons:
			for person2 in self.persons:
				if person1 is person2:
					continue
				if self.__isExist(fromPerson=person2, toPerson=person1, tallyList=tallyList):
					continue
				tally = {'from': person1, 'to': person2, 'amount': self.amountDebt(person1, person2), 'status': 'unpaid'}
				tallyList.append(tally)
		self.__setPositiveAmountDebt(tallyList)
		return tallyList

	@staticmethod
	def __setPositiveAmountDebt(tallyList: list):
		for tally in tallyList:
			if tally['amount'] < 0:
				creditor = tally['from']
				debtor = tally['to']
				amount = abs(tally['amount'])
				tallyList.remove(tally)
				newTally = {'from': debtor, 'to': creditor, 'amount': amount, 'status': 'unpaid'}
				tallyList.append(newTally)

	@staticmethod
	def __isExist(fromPerson: person.Person, toPerson: person.Person, tallyList: list):
		for tally in tallyList:
			if fromPerson is tally['from'] and toPerson is tally['to']:
				return True
		return False

	def amountDebt(self, person1: person.Person, person2: person.Person):
		amount = 0
		if person1 is person2:
			return amount
		for record in self.records:
			if person1 is record.buyer and person2 in record.users:
				amount += record.userDebt[person2]
			elif person2 is record.buyer and person1 in record.users:
				amount -= record.userDebt[person1]
		return amount

	@property
	def records(self):
		records = list()
		records.extend(self.__debts)
		records.extend(self.__records)
		for meet in self.__meets:
			records.extend(meet.records)
		return records

	@property
	def cost(self):
		cost = 0
		for record in self.records:
			cost += record.cost
		return cost

	def __repr__(self):
		result = ''
		for d in self.tallyList:
			result += f"{str(d['from'])} to {str(d['to'])}: {d['amount']}\n"
		return result