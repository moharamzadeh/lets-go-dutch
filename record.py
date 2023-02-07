import person

class Record:
	def __init__(self, title, buyer: person.Person, dateTime=None):
		self.title = title
		self.buyer = buyer
		self.dateTime = dateTime
		self.userDebt = dict()

	@property
	def cost(self):
		cost = 0
		for debt in self.userDebt.values():
			cost += debt
		return cost

	@property
	def persons(self):
		persons = set(self.userDebt.keys())
		persons.add(self.buyer)
		return persons

	@property
	def users(self):
		users = self.persons.copy()
		users.remove(self.buyer)
		return users

	def addUser(self, user: person.Person, amount):
		self.userDebt[user] = amount

	def addUsers(self, userAmount: dict):
		for user in userAmount:
			self.addUser(user, userAmount[user])

	def __getitem__(self, person: person.Person):
		return self.userDebt[person]

	def __repr__(self):
		result = f"{self.title} ->\t{str(self.buyer)}: "
		for person in self.userDebt:
			result += f"{str(person)} {self.userDebt[person]}  "
		return result