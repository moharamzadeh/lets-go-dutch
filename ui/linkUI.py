from widgetAccess import *

class LinkUI(WidgetAccess):
	def __init__(self):
		app = QApplication(sys.argv)

		super()._createWindow()
		self._createLayout()

		sys.exit(app.exec_())

	def _createLayout(self):
		super()._createLayout()
		self._setLink()

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
		if ok:
			self.debtList.addItem(text)

	def _clickBtnAddRecord(self):
		text, ok = QInputDialog.getText(self.widget, 'نام رکورد', 'نام رکورد را وارد کنید:')
		if ok:
			self.recordList.addItem(text)

	def _clickBtnAddMeet(self):
		text, ok = QInputDialog.getText(self.widget, 'نام قرار', 'نام قرار را وارد کنید:')
		if ok:
			self.meetList.addItem(text)

	def _clickBtnAddPerson(self):
		text, ok = QInputDialog.getText(self.widget, 'نام فرد', 'نام فرد را وارد کنید:')
		if ok:
			self.personList.addItem(text)

	def _clickBtnAddTally(self):
		text, ok = QInputDialog.getText(self.widget, 'نام قرار', 'نام قرار را وارد کنید:')
		if ok:
			self.tallyList.addItem(str(text))

if __name__ == '__main__':
	linkUI = LinkUI()