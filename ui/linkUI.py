from mainMenu import *

class LinkUI(Window):
	def __init__(self):
		app = QApplication(sys.argv)

		super()._createWindow()
		self._createLayout()

		sys.exit(app.exec_())

	def _createLayout(self):
		super()._createLayout()
		self.btnAddTally.clicked.connect(lambda: self.clickBntAddTally())

	@property
	def btnAddTally(self):
		return self.tallyWidget.layout().itemAt(0).itemAt(0).widget()

	def clickBntAddTally(self):
		print('hello')
		# self.mainSplitter.widge

if __name__ == '__main__':
	linkUI = LinkUI()