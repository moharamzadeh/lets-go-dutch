from widgetAccess import *

class LinkUI(WidgetAccess):
	def __init__(self):
		app = QApplication(sys.argv)

		super()._createWindow()
		self._createLayout()

		sys.exit(app.exec_())

	def _createLayout(self):
		super()._createLayout()

if __name__ == '__main__':
	linkUI = LinkUI()