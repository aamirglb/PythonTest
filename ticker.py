import sys
import time
from PySide2 import QtWidgets, QtGui, QtCore

class Ticker(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.offset = 0
		self.mTimerId = 0
		self.myText = ''
		self.setGeometry(50, 100, 300, 100)
		self.progress = QtWidgets.QProgressDialog()
		self.value = 0
		self.progress.setLabelText("Saving ")
		self.progress.setRange(0, 30*10)
		self.progress.setModal(True)
		self.progress.setValue(0)
		self.progress.autoClose = True

	def text(self):
		return self.myText

	def setText(self, newText):
		self.myText = newText
		self.update()
		self.updateGeometry()

	def sizeHint(self):		
		# return QtGui.fontMetrics().size(0, text())
		return self.fontMetrics().size(0, self.text())

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		textWidth = self.fontMetrics().width(self.text())
		if textWidth < 1:
			return
		x = -self.offset
		while x < self.width():
			painter.drawText(x, 0, textWidth, self.height(),
				QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, self.text())
			x += textWidth

	def showEvent(self, event):
		# self.myTimerId = QtCore.QObject.startTimer(30)
		self.myTimerId = self.startTimer(30)

	def timerEvent(self, event):
		if event.timerId() == self.myTimerId:
			self.offset += 1
			if self.offset >= self.fontMetrics().width(self.text()):
				self.offset = 0
			self.scroll(-1, 0)
			if self.value < self.progress.maximum():
				self.value += 1
				self.progress.setValue(self.value)
		else:
			QtWidgets.QWidget.timerEvent(event)

	def hideEvent(self, event):
		self.killTimer(self.myTimerId)
		self.myTimerId = 0				


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	ticker = Ticker()
	ticker.setText(' +++ Qt Event Handling +++ ')
	ticker.show()	
	
	sys.exit(app.exec_())