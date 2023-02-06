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
		recordList.insertItem(0, 'پیتزا')
		recordList.insertItem(1, 'نوشیدنی')
		recordList.insertItem(2, 'تاکسی')
		recordList.setCurrentRow(0)
		return recordList

	def __createSplitter(self, layout: QHBoxLayout):
		topRight = self.__getTallyList()
		bottomRight = QVBoxLayout()
		btn = QPushButton('افزودن')
		bottomRight.addWidget(btn)

		rightLayout = QVBoxLayout()
		rightLayout.addWidget(topRight)
		rightLayout.addLayout(bottomRight)

		rightWidget = QWidget()
		rightWidget.setLayout(rightLayout)
		

		centerTop = self.__getMeetList()
		centerBottom = QTextBrowser()
		centerBottom.setText(
			'''
			عرفان به علی ۱۰۰۰
			حسین به علی ۲۰۰۰
			حسین به عرفان ۵۰۰۰
			'''
		)

		centerLayout = QVBoxLayout()
		centerLayout.addWidget(centerTop)
		centerLayout.addWidget(centerBottom)

		centerWidget = QWidget()
		centerWidget.setLayout(centerLayout)


		leftTop = self.__getRecordList()
		leftBotton = QTableWidget()
		leftBotton.setColumnCount(2)
		leftBotton.setRowCount(20)

		leftLayout = QVBoxLayout()
		leftLayout.addWidget(leftTop)
		leftLayout.addWidget(leftBotton)

		leftWidget = QWidget()
		leftWidget.setLayout(leftLayout)



		splitter = QSplitter(Qt.Horizontal)
		splitter.setLayoutDirection(Qt.RightToLeft)
		splitter.addWidget(rightWidget)
		splitter.addWidget(centerWidget)
		splitter.addWidget(leftWidget)

		splitter.setSizes([10, 200, 300])

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