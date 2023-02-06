import record
import person

class SameCost(record.Record):
	def __init__(self, title, buyer: person.Person, amount, dateTime=None):
		self.title = title
		self.buyer = buyer
		self.amount = amount
		self.dateTime = dateTime
		self.userDebt = dict()
		self.allPerson = {self.buyer}

	def addUser(self, person: person.Person):
		self.allPerson.add(person)
		self.__computDebts()

	def __computDebts(self):
		for user in self.allPerson:
			if user is self.buyer:
				continue
			self.userDebt[user] = self.amount / len(self.allPerson)