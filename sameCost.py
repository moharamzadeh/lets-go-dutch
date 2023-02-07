import record
import person

class SameCost(record.Record):
	def __init__(self, title, buyer: person.Person, amount, dateTime=None):
		super().__init__(title, buyer, dateTime)
		self.amount = amount
		self.__allPerson = {self.buyer}

	@property
	def cost(self):
		return self.amount

	def addUser(self, person: person.Person):
		self.__allPerson.add(person)
		self.__computDebts()

	def __computDebts(self):
		for user in self.__allPerson:
			if user is self.buyer:
				continue
			self.userDebt[user] = self.amount / len(self.__allPerson)