import sys
from PySide2 import QtWidgets, QtGui, QtCore

class MyWidget(QtWidgets.QWidget):
	eventCount = 0
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)

	def event(self, _event):
		
		MyWidget.eventCount += 1
		print(f'event count: {MyWidget.eventCount}, Type: {_event.type()}')

if __name__ == "__main__":
	app =  QtWidgets.QApplication(sys.argv)
	widget =MyWidget()
	widget.show()
	sys.exit(app.exec_())
			