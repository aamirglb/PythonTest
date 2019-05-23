import sys
import math
from PySide2 import QtWidgets, QtGui, QtCore


class Test(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(Test, self).__init__(parent)
		self.angle = 150
		self.setBackgroundRole(QtGui.QPalette.Dark)
		self.setAutoFillBackground(True)
		self.value = 0
		self.maxValue = 100
		self.counter = -1

	def sizeHint(self):
		return QtCore.QSize(120*2, 120*2)

	def setCautionRange(self, min, max):
		self.cautionMin = min
		self.cautionMax = max

	def setWarningRange(self, min, max):
		self.warningMin = min
		self.warningMax = max

	def setNormalRange(self, min, max):
		self.normalMin = min
		self.normalMax = max

	@QtCore.Slot(int)
	def setDialValue(self, _val):
		self.value = _val

		self.angle = 150 + (210 * self.value) // self.maxValue

		self.update()

	@QtCore.Slot(int)
	def setRotationAngle(self, _angle):
		self.angle = _angle
		self.update()

	@QtCore.Slot()
	def timeout(self):
		self.counter += 1
		self.update()

	def keyPressEvent(self, event):
		self.counter += 1
		print('key pressed')
		self.update()


	def drawFilledArc(self, painter, startAngle, endAngle, minRadius, majRadius, color):

		minBoundingRect = QtCore.QRectF(-minRadius, -minRadius, minRadius*2, minRadius*2)
		majBoundingRect = QtCore.QRectF(-majRadius, -majRadius, majRadius*2, majRadius*2)

		arcPath = QtGui.QPainterPath()
		# draw first line		
		arcPath.moveTo(minRadius * math.cos(-startAngle * math.pi / 180.0), 
			minRadius * math.sin(-startAngle * math.pi / 180))
		arcPath.lineTo(majRadius * math.cos(-startAngle * math.pi / 180.0), 
			majRadius * math.sin(-startAngle * math.pi / 180))

		arcLength = endAngle - startAngle
		arcPath.arcTo(majBoundingRect, startAngle, arcLength)

		arcPath.lineTo(minRadius * math.cos(-endAngle * math.pi / 180.0), minRadius * math.sin(-endAngle * math.pi / 180))
		arcPath.arcTo(minBoundingRect, endAngle, -arcLength)
		arcPath.arcMoveTo(minBoundingRect, startAngle)
		arcPath.closeSubpath()
		painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
		painter.setBrush(QtGui.QBrush(QtGui.QColor(color)))
		painter.drawPath(arcPath)

	def preRenderFixedItems(self):
		pass

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		side = min(self.width(), self.height())
		painter.setViewport((self.width() - side) / 2, (self.height() - side) / 2,
			side, side)

		painter.setWindow(-self.width()/2, -self.height()/2, self.width(), self.height())
		painter.setRenderHint(QtGui.QPainter.Antialiasing, True)

		# Radius of the needle drawn from (0, 0)
		radius = 90 + 5

		painter.save()		
		painter.rotate(self.angle)
		palette = QtGui.QPalette()

		needleBaseWidth = 5
		needlePath = QtGui.QPainterPath()
		needlePath.moveTo(0, needleBaseWidth)
		needlePath.lineTo(radius, 0)
		needlePath.lineTo(0, -needleBaseWidth)
		needlePath.lineTo(0, needleBaseWidth)
			
		painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
		painter.setBrush(palette.brush(QtGui.QPalette.Active, QtGui.QPalette.Light))
		painter.drawPath(needlePath)
		
		painter.setBrush(QtCore.Qt.black)
		painter.drawEllipse(-10, -10, 20, 20)
		painter.restore()

		# Compute percentage of different arc
		warningValue =  (self.warningMax - self.warningMin)
		cautionValue =  (self.cautionMax - self.cautionMin)
		normalValue =  (self.normalMax - self.normalMin)

		warningArcAngle = (warningValue * (360 - 150) / 100) + 1
		cautionArcAngle = (cautionValue * (360 - 150) / 100) + 1
		normalArcangle = (normalValue * (360 - 150) / 100)
		print(warningValue, cautionValue, normalValue, warningArcAngle, cautionArcAngle, normalArcangle)
		self.drawFilledArc(painter, 0, warningArcAngle, 90, 110, "red")		
		self.drawFilledArc(painter, warningArcAngle, (warningArcAngle + cautionArcAngle), 90, 110, "yellow")
		self.drawFilledArc(painter, (warningArcAngle + cautionArcAngle), (warningArcAngle + cautionArcAngle + normalArcangle), 90, 110, "lime")

		# Write value text
		font = painter.font()
		font.setPixelSize(24)
		painter.setFont(font)
		
		rect = QtCore.QRect(5, 15, 95, 25)
		painter.setBrush(QtCore.Qt.black)
		painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
		painter.drawRect(5, 15, 95, 25)

		painter.setPen(QtGui.QPen(QtGui.QColor("lime"), 2))
		painter.drawText(rect, QtCore.Qt.AlignRight, f"{self.value}")		

	# Property for needle angle
	rotationAngle = QtCore.Property(int, fset=setRotationAngle)

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

	dial = Test()
	
	dial.setNormalRange(0, 70)
	dial.setCautionRange(71, 85)
	dial.setWarningRange(86, 100)

	slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
	slider.setRange(0, 100)
	slider.setValue(0)
	slider.valueChanged.connect(dial.setDialValue)

	spinbox = QtWidgets.QSpinBox()
	spinbox.setRange(0, 100)
	spinbox.setValue(0)
	spinbox.valueChanged.connect(slider.setValue)
	slider.valueChanged.connect(spinbox.setValue)

	animation = QtCore.QPropertyAnimation(slider, b"value")
	animation.setDuration(6000)
	animation.setStartValue(0)
	animation.setEndValue(100)
	animation.finished.connect(animationFinished)
	# animation.start()	

	layout1 = QtWidgets.QHBoxLayout()	
	layout1.addWidget(slider)
	layout1.addWidget(spinbox)

	layout = QtWidgets.QVBoxLayout()
	layout.addWidget(dial)
	layout.addLayout(layout1)

	mainWindow = QtWidgets.QWidget()
	mainWindow.setLayout(layout)
	mainWindow.show()
	
	timer = QtCore.QTimer()
	timer.setInterval(2000)
	timer.timeout.connect(dial.timeout)
	timer.start()
	sys.exit(app.exec_())	