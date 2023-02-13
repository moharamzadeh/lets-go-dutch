from widgets import *

class LinkUI(Widgets):
	def __init__(self):
		super().__init__()
		self.__btnLink()
		self.__selectList()

	def __selectList(self):
		self.listTally.currentRowChanged.connect(self.__selectListTally)

	def __selectListTally(self, i):
		self.stackListPerson.setCurrentIndex(i+1)
	
	def __btnLink(self):
		self.__linkAddTally()
		self.__linkAddPerson()

	def __linkAddTally(self):
		self.btnAddTally.clicked.connect(lambda: self.__dialogAddTally())

	def __linkAddPerson(self):
		self.btnAddPerson.clicked.connect(lambda: self.__dialogAddPerson())

	def __dialogAddTally(self):
		title, ok = QInputDialog.getText(self.widget, 'نام حساب', 'نام حساب را وارد کنید:')
		tallyItem = QListWidgetItem(title)
		if ok:
			self.listTally.addItem(tallyItem)
			self.listTally.setCurrentItem(tallyItem)
			persons = QListWidget()
			self.stackListPerson.addWidget(persons)
			self.stackListPerson.setCurrentWidget(persons)

	def __dialogAddPerson(self):
		name, ok = QInputDialog.getText(self.widget, 'نام فرد', 'نام فرد را وارد کنید:')
		personItem = QListWidgetItem(name)
		if ok:
			self.stackListPerson.currentWidget().addItem(personItem)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	linkUI = LinkUI()
	sys.exit(app.exec_())