from mainMenu import *

class WidgetAccess(Window):
	def __init__(self):
		app = QApplication(sys.argv)

		super()._createWindow()
		self._createLayout()

		sys.exit(app.exec_())

	def _createLayout(self):
		super()._createLayout()

	@property
	def btnAddTally(self):
		return self.tallyWidget.layout().itemAt(0).itemAt(0).widget()

	@property
	def btnDeleteTally(self):
		return self.tallyWidget.layout().itemAt(0).itemAt(1).widget()

	@property
	def tallyList(self) -> QListWidget:
		return self.tallyWidget.layout().itemAt(1).widget()

	@property
	def btnAddPerson(self):
		return self.personWidget.layout().itemAt(0).itemAt(0).widget()

	@property
	def btnDeletePerson(self):
		return self.personWidget.layout().itemAt(0).itemAt(1).widget()

	@property
	def personList(self):
		return self.personWidget.layout().itemAt(1).widget()

	@property
	def btnAddMeet(self):
		return self.meetWidget.layout().itemAt(0).itemAt(0).widget()

	@property
	def btnDeleteMeet(self):
		return self.meetWidget.layout().itemAt(0).itemAt(1).widget()

	@property
	def meetList(self):
		return self.meetWidget.layout().itemAt(1).widget()

	@property
	def btnAddRecord(self):
		return self.recordWidget.layout().itemAt(0).itemAt(0).widget()

	@property
	def recordList(self):
		return self.recordWidget.layout().itemAt(1).widget()

	@property
	def btnDeleteRecord(self):
		return self.recordWidget.layout().itemAt(0).itemAt(1).widget()


	@property
	def btnAddDebt(self):
		return self.debtWidget.layout().itemAt(0).itemAt(0).widget()

	@property
	def btnDeleteDebt(self):
		return self.debtWidget.layout().itemAt(0).itemAt(1).widget()

	@property
	def debtList(self):
		return self.debtWidget.layout().itemAt(1).widget()