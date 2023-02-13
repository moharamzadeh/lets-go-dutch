import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window():
	def __init__(self):
		self._createMainWindow()
		self._createMainLayout()
		self._createMainWidget()

		self.window.show()

	def _createMainWindow(self):
		self.window = QMainWindow()
		self.window.setWindowTitle('محاسبه دنگ')
		self.window.showMaximized()
		self.window.setMinimumHeight(400)
		self.window.setMinimumWidth(800)

	def _createMainLayout(self):
		self.layout = QHBoxLayout()
		self.layout.setDirection(QHBoxLayout.RightToLeft)

	def _createMainWidget(self):
		self.widget = QWidget()
		self.widget.setLayout(self.layout)
		self.window.setCentralWidget(self.widget)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())