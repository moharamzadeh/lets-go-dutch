import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window():
	def __init__(self):
		app = QApplication(sys.argv)

		self.__createWidget()
		self.__createLayout()

		sys.exit(app.exec_())

	def __createWidget(self):
		self.window = QMainWindow()
		self.window.setWindowTitle('محاسبه دنگ')
		self.window.showMaximized()
		self.window.show()

	def __createLayout(self):
		self.__createMenuBar()
	
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
		msg.buttonClicked.connect(exit)
		retval = msg.exec_()


if __name__ == '__main__':
	window = Window()