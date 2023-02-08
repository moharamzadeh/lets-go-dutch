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
		tallyList.insertItem(0, 'انزلی')
		tallyList.insertItem(1, 'آخر ترم')
		tallyList.setCurrentRow(0)
		return tallyList

	def __getMeetList(self):
		meetList = QListWidget()
		meetList.insertItem(0, 'شام')
		meetList.insertItem(1, 'ناهار')
		meetList.insertItem(2, 'پاساژ')
		meetList.setCurrentRow(0)
		return meetList

	def __getRecordList(self):
		recordList = QListWidget()
		recordList.insertItem(0, 'پیتزا\t(خریدار: عرفان)')
		recordList.insertItem(1, 'نوشیدنی')
		recordList.insertItem(2, 'تاکسی')
		recordList.setCurrentRow(0)
		return recordList

	def __getDebtTable(self):
		debtTable = QTableWidget()
		debtTable.setColumnCount(4)
		debtTable.setRowCount(20)
		return debtTable

	def __getPersonList(self):
		personList = QListWidget()
		personList.insertItem(0, 'عرفان')
		personList.insertItem(1, 'علی')
		personList.insertItem(2, 'امیررضا')
		personList.setCurrentRow(0)
		return personList

	def __tallyWidget(self):
		tallyWidget = QWidget()
		tallyLayout = QVBoxLayout()
		tallyWidget.setLayout(tallyLayout)
		
		tallyList = self.__getTallyList()

		btnAddTally = QPushButton('افزودن حساب')
		btnDeleteTally = QPushButton('حذف حساب')

		tallyLayout.addWidget(btnAddTally)
		tallyLayout.addWidget(btnDeleteTally)
		tallyLayout.addWidget(tallyList)
		return tallyWidget

	def __meetWidget(self):
		meetWidget = QWidget()
		meetLayout = QVBoxLayout()
		meetWidget.setLayout(meetLayout)

		meetList = self.__getMeetList()

		btnAddMeet = QPushButton('افزودن قرار')

		meetLayout.addWidget(btnAddMeet)
		meetLayout.addWidget(meetList)
		return meetWidget

	def __personWidget(self):
		personWidget = QWidget()
		personLayout = QVBoxLayout()
		personWidget.setLayout(personLayout)
		personList = self.__getPersonList()
		btnAddPerson = QPushButton('افزودن فرد')
		personLayout.addWidget(btnAddPerson)
		personLayout.addWidget(personList)
		return personWidget

	def __createSplitter(self, layout: QHBoxLayout):
		tallyWidget = self.__tallyWidget()
		meetWidget = self.__meetWidget()


		leftWidget = QWidget()
		leftLayout = QHBoxLayout()
		leftWidget.setLayout(leftLayout)
		recordLayout = QVBoxLayout()
		debtLayout = QVBoxLayout()

		leftLayout.addLayout(recordLayout)
		leftLayout.addLayout(debtLayout)

		btnAddRecord = QPushButton('افزودن رکورد')
		recordList = self.__getRecordList()
		recordLayout.addWidget(btnAddRecord)
		recordLayout.addWidget(recordList)

		personWidget = self.__personWidget()

		result = QTextBrowser()

		personResultSplitter = QSplitter(Qt.Horizontal)
		personResultSplitter.addWidget(result)
		personResultSplitter.addWidget(personWidget)

		debtPersonSplitter = QSplitter(Qt.Vertical)
		debtList = self.__getDebtTable()
		debtPersonSplitter.addWidget(debtList)
		debtPersonSplitter.addWidget(personResultSplitter)



		splitter = QSplitter(Qt.Horizontal)
		splitter.setLayoutDirection(Qt.RightToLeft)
		splitter.addWidget(tallyWidget)
		splitter.addWidget(meetWidget)
		splitter.addWidget(leftWidget)
		splitter.addWidget(debtPersonSplitter)

		splitter.setSizes([1, 1, 1, 150])

		layout.addWidget(splitter)
		
	
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


if __name__ == '__main__':
	window = Window()