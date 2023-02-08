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

	def __setBtnAddTally(self):
		self.btnAddTally.clicked.connect(lambda: self._clickBtnAddTally())

	def _clickBtnAddTally(self):
		text, ok = QInputDialog.getText(self.widget, 'نام قرار', 'نام قرار را وارد کنید:')
		if ok:
			self.tallyList.addItem(str(text))

if __name__ == '__main__':
	linkUI = LinkUI()