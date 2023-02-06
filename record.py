import person

class Record:
	def __init__(self, title, buyer: person.Person, dateTime=None):
		self.title = title
		self.buyer = buyer
		self.dateTime = dateTime
		self.personDebt = dict()

	@property
	def persons(self):
		persons = set(self.personDebt.keys())
		persons.add(self.buyer)
		return persons

	def __setitem__(self, person: person.Person, amount):
		self.personDebt[person] = amount

	def __getitem__(self, person: person.Person):
		return self.personDebt[person]

	def __contains__(self, person: person.Person):
		persons = self.persons.copy()
		persons.remove(self.buyer)
		if person in persons:
			return True
		return False

	def __repr__(self):
		result = f"{self.title} ->\t{str(self.buyer)}: "
		for person in self.personDebt:
			result += f"{str(person)} {self.personDebt[person]}  "
		return result