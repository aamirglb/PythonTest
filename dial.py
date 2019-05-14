import sys
import math

from PySide2 import QtWidgets, QtGui, QtCore

class Dial(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(Dial, self).__init__(parent)
		self.width = 220
		self.height = 180
		self.maxValue = 100
		self.value = 0
		self.angle = 0

	def sizeHint(self):
		return QtCore.QSize(self.width, self.height)

	def setCautionRange(self, min, max):
		self.cautionMin = min
		self.cautionMax = max

	def setWarningRange(self, min, max):
		self.warningMin = min
		self.warningMax = max

	def setNormalRange(self, min, max):
		self.normalMin = min
		self.normalMax = max

	def setValue(self, value):
		if value > self.maxValue:
			self.value = self.maxValue
		else:
			self.value = value
		self.angle = 210 - ((210 * self.value)/self.maxValue)
		self.update()

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		painter.save()
		painter.setRenderHint(QtGui.QPainter.Antialiasing, True);

		painter.drawPoint(125, 105)
		pen = QtGui.QPen(QtGui.QColor("lime"), 6)
		painter.setPen(pen)
		painter.drawArc(50, 30, 150, 150, 0, 16 * 210)
		
		painter.setPen(QtGui.QPen(QtCore.Qt.green, ))

		if self.value <= self.normalMax:
			painter.setPen(QtGui.QPen(QtCore.Qt.green, 6))
			painter.setBrush(QtCore.Qt.green)
		elif self.value >= self.cautionMin and self.value <= self.cautionMax:
			painter.setPen(QtGui.QPen(QtCore.Qt.yellow, 6))
			painter.setBrush(QtCore.Qt.yellow)
		else:
			painter.setPen(QtGui.QPen(QtCore.Qt.red, 6))
			painter.setBrush(QtCore.Qt.red)

		degree = 360 - self.angle

		xPos = (75 + 5) * (math.cos(degree * math.pi / 180.0)) + 125
		yPos = (75 + 5) * (math.sin(degree * math.pi / 180.0)) + 105
		painter.drawLine(125, 105, xPos, yPos)

		# painter.setPen(QtGui.QPen(QtCore.Qt.red))
		painter.drawLine(195, 105, 200, 105)
		painter.drawPie(56, 36, 150, 150, 16 * 210, -16 * (210 - self.angle))

		painter.restore()		

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	widget = Dial()
	widget.setNormalRange(0, 70)
	widget.setCautionRange(71, 85)
	widget.setWarningRange(86, 100)
	widget.setValue(10)

	slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
	slider.setRange(1, 120)
	slider.setValue(10)
	slider.valueChanged.connect(widget.setValue)

	layout = QtWidgets.QVBoxLayout()
	layout.addWidget(widget)
	layout.addWidget(slider)

	mainWindow = QtWidgets.QWidget()
	mainWindow.setLayout(layout)
	mainWindow.show()
	sys.exit(app.exec_())
