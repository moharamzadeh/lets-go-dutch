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
		self.window.setMinimumWidth(600)
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
		self.__createMenuBar()

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

	def __createSplitter(self, layout: QHBoxLayout):
		tallyWidget = QWidget()
		tallyLayout = QVBoxLayout()
		tallyWidget.setLayout(tallyLayout)
		
		tallyList = self.__getTallyList()

		btnAddTally = QPushButton('افزودن حساب')
		btnDeleteTally = QPushButton('حذف حساب')
		btnAddPerson = QPushButton('ایجاد فرد')
		btnComput = QPushButton('محاسبه')

		tallyLayout.addWidget(tallyList)
		tallyLayout.addWidget(btnAddTally)
		tallyLayout.addWidget(btnDeleteTally)
		tallyLayout.addWidget(btnAddPerson)
		tallyLayout.addWidget(btnComput)

		meetList = self.__getMeetList()

		meetLayout = QVBoxLayout()
		meetLayout.addWidget(meetList)

		btnAddMeet = QPushButton('افزودن قرار')
		meetLayout.addWidget(btnAddMeet)

		meetWidget = QWidget()
		meetWidget.setLayout(meetLayout)


		leftBotton = QTableWidget()
		leftBotton.setColumnCount(3)
		leftBotton.setRowCount(20)

		leftTopTabRecord = self.__getRecordList()
		leftTopTabbleDebt = self.__getDebtTable()

		leftTopLayout = QHBoxLayout()
		leftTopLayout.addWidget(leftTopTabRecord)
		leftTopLayout.addWidget(leftTopTabbleDebt)

		leftTop = QWidget()
		leftTop.setLayout(leftTopLayout)

		leftLayout = QVBoxLayout()
		leftLayout.addWidget(leftTop)
		leftLayout.addWidget(leftBotton)

		leftWidget = QWidget()
		leftWidget.setLayout(leftLayout)



		splitter = QSplitter(Qt.Horizontal)
		splitter.setLayoutDirection(Qt.RightToLeft)
		splitter.addWidget(tallyWidget)
		splitter.addWidget(meetWidget)
		splitter.addWidget(leftWidget)

		splitter.setSizes([1, 60, 250])

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
		msg.setText('می‌خواهید از برنامه خارج شوید؟')
		msg.setWindowTitle('خروج')
		msg.layoutDirection()
		msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)

		retval = msg.exec_()
		if retval == QMessageBox.Yes:
			self.window.close()


if __name__ == '__main__':
	window = Window()