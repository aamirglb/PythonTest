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
		painter.setPen(QtGui.QPen(QtGui.QColor("lime"), 10))
		painter.drawArc(50, 30, 150, 150, 16 * 210, -16 * (210 - 60))

		painter.setPen(QtGui.QPen(QtGui.QColor("yellow"), 10))
		painter.drawArc(50, 30, 150, 150, 16 * 61, -16 * (60 - 20))
		
		painter.setPen(QtGui.QPen(QtGui.QColor("red"), 10))
		painter.drawArc(50, 30, 150, 150, 0, 16 * 19)

		# painter.setPen(QtGui.QPen(QtCore.Qt.green, ))

		# if self.value <= self.normalMax:
		# 	painter.setPen(QtGui.QPen(QtCore.Qt.green, 6))
		# 	painter.setBrush(QtCore.Qt.green)
		# elif self.value >= self.cautionMin and self.value <= self.cautionMax:
		# 	painter.setPen(QtGui.QPen(QtCore.Qt.yellow, 6))
		# 	painter.setBrush(QtCore.Qt.yellow)
		# else:
		# 	painter.setPen(QtGui.QPen(QtCore.Qt.red, 6))
		# 	painter.setBrush(QtCore.Qt.red)

		degree = 360 - self.angle

		painter.setPen(QtGui.QPen(QtGui.QColor("green"), 2))
		xPos = (75 + 5) * (math.cos(degree * math.pi / 180.0)) + 125
		yPos = (75 + 5) * (math.sin(degree * math.pi / 180.0)) + 105
		painter.drawLine(125, 105, xPos, yPos)

		x = xPos + (math.cos(-1 * math.pi / 180.0)) * (75+5)
		y = yPos + (math.sin(-1 * math.pi / 180.0)) * (75+5)

		

		painter.save()
		# transform = QtGui.QTransform()
		# transform.translate(xPos-75, yPos-75)
		# transform.rotate(degree)
		
		# painter.setWorldTransform(transform)
		# painter.drawEllipse(QtCore.QPointF(xPos, yPos), 150, 150)
		# transform.translate(xPos+75, yPos+75)
		# painter.translate(x, y)
		
		
		# print(xPos, yPos, x, y)
		
		# painter.drawLine(xPos, yPos, x, y)
		# painter.drawLine(x, y, 125, 105)
		# painter.rotate(-self.angle)
		painter.restore()
		# needle = QtGui.QPainterPath()
		# needle.moveTo(xPos, yPos)
		# x = xPos * (math.cos(20 * math.pi / 180.0)) + 0
		# y = yPos * (math.sin(20 * math.pi / 180.0)) + 0		
		# needle.lineTo(x, y)
		# needle.lineTo(125, 105)
		# needle.lineTo(127, 105)		
		# needle.closeSubpath()
		# painter.drawPath(needle)
		# painter.drawLine(125, 105, xPos, yPos)

		# painter.setPen(QtGui.QPen(QtCore.Qt.red))
		# painter.drawLine(195, 105, 200, 105)
		# painter.drawPie(56, 36, 150, 150, 16 * 210, -16 * (210 - self.angle))

		painter.restore()


		# starPath = QtGui.QPainterPath()
		# starPath.moveTo(90, 50)
		# for i in range(0, 5):    		
		# 	starPath.lineTo(50 + 40 * math.cos(0.8 * i * math.pi),
		#                 50 + 40 * math.sin(0.8 * i * math.pi))
		# starPath.closeSubpath()
		# painter.drawPath(starPath)		

def animationFinished():
	if animation.currentValue() == 100:
		animation.setStartValue(100)
		animation.setEndValue(0)
	else:
		animation.setStartValue(0)
		animation.setEndValue(100)		
	animation.start()


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

	animation = QtCore.QPropertyAnimation(slider, b"value")
	animation.setDuration(10000)
	# animation.setLoopCount(2)
	animation.setStartValue(0)
	animation.setEndValue(100)
	animation.finished.connect(animationFinished)
	
	

	layout = QtWidgets.QVBoxLayout()
	layout.addWidget(widget)
	layout.addWidget(slider)

	mainWindow = QtWidgets.QWidget()
	mainWindow.setLayout(layout)
	mainWindow.show()
	animation.start()
	sys.exit(app.exec_())
