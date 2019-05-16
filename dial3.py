import sys
from PySide2 import QtWidgets, QtGui, QtCore


class Test(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(Test, self).__init__(parent)
		self.angle = 210
		self.setBackgroundRole(QtGui.QPalette.Dark)
		self.setAutoFillBackground(True)
		self.value = 0

	def sizeHint(self):
		return QtCore.QSize(400, 400)

	@QtCore.Slot(int)
	def setDialValue(self, _val):
		self.value = _val

		self.angle = (210 * self.value)//100

		self.update()

	@QtCore.Slot(int)
	def setRotationAngle(self, _angle):
		self.angle = _angle
		self.update()

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		painter.setWindow(-200, -200, 400, 400)
		painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
		painter.drawRect(-195, -195, 390, 390)

		# Test
		painter.drawLine(-200, 0, 200, 0)
		painter.drawLine(0, -200, 0, 200)
		radius = 90

		painter.save()
		painter.rotate(360 - self.angle)

		palette = QtGui.QPalette()

		needlePath = QtGui.QPainterPath()
		needlePath.moveTo(0, 3)
		needlePath.lineTo(radius, 0)
		needlePath.lineTo(0, -3)
		needlePath.lineTo(0, 3)
		# needlePath.closeSubpath()

		painter.fillPath(needlePath, QtGui.QBrush(QtGui.QColor("lime")))
		painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
		painter.setBrush(palette.brush(QtGui.QPalette.Active, QtGui.QPalette.Light))
		painter.drawPath(needlePath)
		# painter.setPen(QtGui.QPen(QtCore.Qt.red, 3))
		# painter.drawPoint(0, 0)
		# painter.drawPoint(radius, 0)
		painter.restore()
		origin = QtCore.QPoint(-90, -90)
		width = 180
		height = 180

		penWidth = 15
		painter.setPen(QtGui.QPen(QtGui.QColor("lime"), penWidth))
		painter.drawArc(origin.x(), origin.y(), width, height, 16 * 210, -16 * (210 - 60))

		painter.setPen(QtGui.QPen(QtGui.QColor("yellow"), penWidth))
		painter.drawArc(origin.x(), origin.y(), width, height, 16 * 61, -16 * (60 - 20))
		
		painter.setPen(QtGui.QPen(QtGui.QColor("red"), penWidth))
		painter.drawArc(origin.x(), origin.y(), width, height, 0, 16 * 19)

		# Write value text
		font = painter.font()
		font.setPixelSize(24)
		painter.setFont(font)

		
		rect = QtCore.QRect(1, 10, 95, 25)
		painter.setBrush(QtCore.Qt.black)
		painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
		painter.drawRect(1, 10, 95, 25)

		painter.setPen(QtGui.QPen(QtGui.QColor("lime"), 2))
		painter.drawText(rect, QtCore.Qt.AlignRight, f"{self.value}")

		# painter.drawText()


	rotationAngle = QtCore.Property(int, fset=setRotationAngle)

def animationFinished():
	if animation.currentValue() == 210:
		animation.setStartValue(210)
		animation.setEndValue(0)
	else:
		animation.setStartValue(0)
		animation.setEndValue(210)		
	animation.start()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)

	dial = Test()
	
	slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
	slider.setRange(1, 100)
	slider.setValue(0)
	slider.valueChanged.connect(dial.setDialValue)

	animation = QtCore.QPropertyAnimation(dial, b"rotationAngle")
	animation.setDuration(5000)
	animation.setStartValue(210)
	animation.setEndValue(0)
	animation.finished.connect(animationFinished)
	# animation.start()

	layout = QtWidgets.QVBoxLayout()
	layout.addWidget(dial)
	layout.addWidget(slider)

	mainWindow = QtWidgets.QWidget()
	mainWindow.setLayout(layout)
	mainWindow.show()
	
	sys.exit(app.exec_())	