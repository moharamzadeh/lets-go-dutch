from mainMenu import *

class LinkUI(Window):
	def __init__(self):
		app = QApplication(sys.argv)

		super()._createWindow()
		self._createLayout()

		sys.exit(app.exec_())

	def _createLayout(self):
		super()._createLayout()
		print(self.Layout.itemAt(0))

	def btnAddTally(self):
		self.mainSplitter.widge

if __name__ == '__main__':
	linkUI = LinkUI()