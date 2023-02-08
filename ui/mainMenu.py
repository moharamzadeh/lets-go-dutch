import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window():
	def __init__(self):
		app = QApplication(sys.argv)

		self.__createWindow()
		self.__createLayout()

		sys.exit(app.exec_())

	def __createWindow(self):
		self.window = QMainWindow()
		self.window.setWindowTitle('محاسبه دنگ')
		self.window.showMaximized()
		self.window.setMinimumHeight(400)
		self.window.setMinimumWidth(800)
		self.__createWidget()
		self.window.show()

	def __createWidget(self):
		self.widget = QWidget()
		self.window.setCentralWidget(self.widget)

	def __createLayout(self):
		layout = QHBoxLayout()
		layout.setDirection(QHBoxLayout.RightToLeft)
		self.widget.setLayout(layout)


		self.__createSplitter(layout)
		# self.__createMenuBar()

	def __getTallyList(self):		
		tallyList = QListWidget()
		return tallyList

	def __getMeetList(self):
		meetList = QListWidget()
		return meetList

	def __getRecordList(self):
		recordList = QListWidget()
		return recordList

	def __getDebtList(self):
		debtList = QListWidget()
		return debtList

	def __getPersonList(self):
		personList = QListWidget()
		return personList

	def __getDetailRecord(self):
		detailRecord = QTableWidget()
		detailRecord.setColumnCount(4)
		detailRecord.setRowCount(20)
		return detailRecord


	def __tallyWidget(self):
		tallyWidget = QWidget()
		tallyLayout = QVBoxLayout()
		btnLayout = QHBoxLayout()
		tallyWidget.setLayout(tallyLayout)
		
		tallyList = self.__getTallyList()

		btnAddTally = QPushButton('افزودن حساب')
		btnDeleteTally = QPushButton('حذف حساب')
		btnLayout.addWidget(btnAddTally)
		btnLayout.addWidget(btnDeleteTally)

		tallyLayout.addLayout(btnLayout)
		tallyLayout.addWidget(tallyList)
		return tallyWidget

	def __meetWidget(self):
		meetWidget = QWidget()
		meetLayout = QVBoxLayout()
		btnLayout = QHBoxLayout()
		meetWidget.setLayout(meetLayout)

		meetList = self.__getMeetList()

		btnAddMeet = QPushButton('افزودن قرار')
		btnDeleteMeet = QPushButton('حذف قرار')
		btnLayout.addWidget(btnAddMeet)
		btnLayout.addWidget(btnDeleteMeet)

		meetLayout.addLayout(btnLayout)
		meetLayout.addWidget(meetList)
		return meetWidget

	def __personWidget(self):
		personWidget = QWidget()
		personLayout = QVBoxLayout()
		btnLayout = QHBoxLayout()
		personWidget.setLayout(personLayout)
		personList = self.__getPersonList()
		btnAddPerson = QPushButton('افزودن فرد')
		btnDeletePerson = QPushButton('حذف فرد')
		btnLayout.addWidget(btnAddPerson)
		btnLayout.addWidget(btnDeletePerson)
		personLayout.addLayout(btnLayout)
		personLayout.addWidget(personList)
		return personWidget

	def __debtWidget(self):
		debtWidget = QWidget()
		debtLayout = QVBoxLayout()
		btnLayout = QHBoxLayout()
		debtWidget.setLayout(debtLayout)
		debtList = self.__getDebtList()
		btnAddDebt = QPushButton('افزودن بدهی')
		btnDeleteDebt= QPushButton('حذف بدهی')
		btnLayout.addWidget(btnAddDebt)
		btnLayout.addWidget(btnDeleteDebt)
		debtLayout.addLayout(btnLayout)
		debtLayout.addWidget(debtList)
		return debtWidget

	def __recordWidget(self):
		recordWidget = QWidget()
		recordLayout = QVBoxLayout()
		btnLayout = QHBoxLayout()
		recordWidget.setLayout(recordLayout)
		btnAddRecord = QPushButton('افزودن رکورد')
		btnDeleteRecord = QPushButton('حذف رکورد')
		btnLayout.addWidget(btnAddRecord)
		btnLayout.addWidget(btnDeleteRecord)
		recordList = self.__getRecordList()
		recordLayout.addLayout(btnLayout)
		recordLayout.addWidget(recordList)
		return recordWidget

	def __createSplitter(self, layout: QHBoxLayout):
		tallyWidget = self.__tallyWidget()
		meetWidget = self.__meetWidget()


		leftWidget = QWidget()
		leftLayout = QHBoxLayout()
		leftWidget.setLayout(leftLayout)		

		recordDebtSplitter = QSplitter(Qt.Vertical)
		recordWidget = self.__recordWidget()
		debtWidget = self.__debtWidget()
		recordDebtSplitter.addWidget(recordWidget)
		recordDebtSplitter.addWidget(debtWidget)

		result = QTextBrowser()

		tallyPersonSplitter = QSplitter(Qt.Vertical)
		personWidget = self.__personWidget()
		tallyPersonSplitter.addWidget(tallyWidget)
		tallyPersonSplitter.addWidget(personWidget)

		detailResultSplitter = QSplitter(Qt.Vertical)
		detailRecord = self.__getDetailRecord()
		detailResultSplitter.addWidget(detailRecord)
		detailResultSplitter.addWidget(result)


		self.mainSplitter = QSplitter(Qt.Horizontal)
		self.mainSplitter.setLayoutDirection(Qt.RightToLeft)
		self.mainSplitter.addWidget(tallyPersonSplitter)
		self.mainSplitter.addWidget(meetWidget)
		self.mainSplitter.addWidget(recordDebtSplitter)
		self.mainSplitter.addWidget(detailResultSplitter)

		self.mainSplitter.setStretchFactor(0, 1)
		self.mainSplitter.setStretchFactor(1, 1)
		self.mainSplitter.setStretchFactor(2, 2)
		self.mainSplitter.setStretchFactor(3, 4)

		layout.addWidget(self.mainSplitter)
		
	
	def __createMenuBar(self):
		menu = self.window.menuBar()
		file = menu.addMenu('File')
		btnNew = file.addAction('New')
		file.addSeparator()
		btnExit = file.addAction('Exit')
		btnExit.triggered.connect(self.__createExitMessage)

		other = menu.addMenu('Help')
		about = other.addAction('About')

	def __createExitMessage(self):
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Warning)
		msg.setText('آیا می‌خواهید از برنامه خارج شوید؟')
		msg.setWindowTitle('خروج')
		msg.layoutDirection()
		msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)

		retval = msg.exec_()
		if retval == QMessageBox.Yes:
			self.window.close()