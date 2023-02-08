from widgetAccess import *
from tally import *

class LinkUI(WidgetAccess):
	def __init__(self):
		app = QApplication(sys.argv)

		self.tallyObjectList = list()

		super()._createWindow()
		self._createLayout()

		sys.exit(app.exec_())

	def _createLayout(self):
		super()._createLayout()
		self._setLink()
		self._setSelect()

	def _setLink(self):
		self.__setBtnAddTally()
		self.__setBtnAddPerson()
		self.__setBtnAddMeet()
		self.__setBtnAddRecord()
		self.__setBtnAddDebt()

	def __setBtnAddTally(self):
		self.btnAddTally.clicked.connect(lambda: self._clickBtnAddTally())

	def __setBtnAddPerson(self):
		self.btnAddPerson.clicked.connect(lambda: self._clickBtnAddPerson())

	def __setBtnAddMeet(self):
		self.btnAddMeet.clicked.connect(lambda: self._clickBtnAddMeet())

	def __setBtnAddRecord(self):
		self.btnAddRecord.clicked.connect(lambda: self._clickBtnAddRecord())

	def __setBtnAddDebt(self):
		self.btnAddDebt.clicked.connect(lambda: self._clickBtnAddDebt())

	def _clickBtnAddDebt(self):
		text, ok = QInputDialog.getText(self.widget, 'نام بدهی', 'نام بدهی را وارد کنید:')
		debtItem = QListWidgetItem(text)
		if ok:
			self.debtList.addItem(debtItem)

	def _clickBtnAddRecord(self):
		text, ok = QInputDialog.getText(self.widget, 'نام رکورد', 'نام رکورد را وارد کنید:')
		recordItem = QListWidgetItem(text)
		if ok:
			self.recordList.addItem(recordItem)

	def _clickBtnAddMeet(self):
		text, ok = QInputDialog.getText(self.widget, 'نام قرار', 'نام قرار را وارد کنید:')
		meetItem = QListWidgetItem(text)
		if ok:
			self.meetList.addItem(meetItem)

	def _clickBtnAddPerson(self):
		text, ok = QInputDialog.getText(self.widget, 'نام فرد', 'نام فرد را وارد کنید:')
		personItem = QListWidgetItem(text)
		if ok:
			self.personList.addItem(personItem)

	def _clickBtnAddTally(self):
		title, ok = QInputDialog.getText(self.widget, 'نام قرار', 'نام قرار را وارد کنید:')
		tallyItem = QListWidgetItem(title)
		if ok:
			self.tallyList.addItem(tallyItem)
			tally = Tally(title)
			self.tallyObjectList.append(tally)

	
	def _setSelect(self):
		self._setSelectTally()

	def _setSelectTally(self):
		self.tallyList.itemClicked.connect(lambda: self.__showTallyDetail())

	def __showTallyDetail(self):
		tallyTitle = self.tallyList.currentItem().text()
		selectedTally = self.search(tallyTitle, self.tallyObjectList)

	def search(self, title: str, list: list):
		for item in list:
			if item.title == title:
				return item

if __name__ == '__main__':
	linkUI = LinkUI()