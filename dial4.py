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
		return QtCore.QSize(400, 400)

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

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		painter.setWindow(-200, -200, 400, 400)
		painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
		painter.drawRect(-195, -195, 390, 390)

		# Test
		painter.drawLine(-200, 0, 200, 0)
		painter.drawLine(0, -200, 0, 200)
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
	
		painter.fillPath(needlePath, QtGui.QBrush(QtGui.QColor("lime")))
		painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
		painter.setBrush(palette.brush(QtGui.QPalette.Active, QtGui.QPalette.Light))
		painter.drawPath(needlePath)
		
		painter.setBrush(QtCore.Qt.black)
		painter.drawEllipse(-10, -10, 20, 20)
		painter.restore()

		painter.save()
		
		width = 180
		height = 180
		origin = QtCore.QPoint(-width/2, -height/2)
		
		painter.restore()

		arcPath = QtGui.QPainterPath()
		startAngle = 210

		##########  Working  ################
		# arcPath.moveTo(90, 0)
		# arcPath.lineTo(110, 0)
		# arcPath.arcTo(-110, -110, 220, 220, 0, 210)
		# arcPath.arcMoveTo(-110, -110, 220, 220, 210)
			
		# startAngle = 360 - 210
		# radius = 90
		# arcPath.lineTo(radius * math.cos(startAngle * math.pi / 180.0), radius * math.sin(startAngle * math.pi / 180))

		# arcPath.arcTo(origin.x(), origin.y(), width, height, 210, -210)
		# arcPath.arcMoveTo(-90, -90, 180, 180, 0)
		########################	

		# Compute percentage of different arc
		warningValue = self.maxValue - (self.warningMax - self.warningMin)
		cautionValue = self.maxValue - (self.cautionMax - self.cautionMin)
		normalValue = self.maxValue - (self.normalMax - self.normalMin)

		warningArcAngle = (warningValue * (360 - 150) // 100)
		cautionArcAngle = (cautionValue * (360 - 150) // 100)
		normalArcangle = (normalValue * (360 - 150) // 100)

		# Warning range
		arcPath.moveTo(90, 0)
		arcPath.lineTo(110, 0)
		arcPath.arcTo(-110, -110, 220, 220, 0, 10)
		arcPath.arcMoveTo(-110, -110, 220, 220, 10)
			
		startAngle = 360 - 10
		radius = 90
		arcPath.lineTo(radius * math.cos(startAngle * math.pi / 180.0), radius * math.sin(startAngle * math.pi / 180))

		arcPath.arcTo(origin.x(), origin.y(), width, height, 10, -10)
		arcPath.arcMoveTo(-90, -90, 180, 180, 10)
		
		arcPath.closeSubpath()
		painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
		painter.setBrush(QtGui.QBrush(QtGui.QColor("red")))
		painter.drawPath(arcPath)
		

		# Caution range
		arc2 = QtGui.QPainterPath()
		startAngle = 360 - 10
		arc2.moveTo(90 * math.cos(startAngle * math.pi / 180.0), 90 * math.sin(startAngle * math.pi / 180))
		arc2.lineTo(110 * math.cos(startAngle * math.pi / 180.0), 110 * math.sin(startAngle * math.pi / 180))
		arc2.arcTo(-110, -110, 220, 220, 11, 30)
		arc2.lineTo(90 * math.cos(320 * math.pi / 180.0), 90 * math.sin(320 * math.pi / 180))
		arc2.arcTo(origin.x(), origin.y(), width, height, 40, -30)
		arc2.arcMoveTo(-90, -90, 180, 180, 40)
		arc2.closeSubpath()
		painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
		painter.setBrush(QtGui.QBrush(QtGui.QColor("yellow")))
		painter.drawPath(arc2)

		# Normal range
		arc3 = QtGui.QPainterPath()
		startAngle = 360 - (10 + 30)
		arc3.moveTo(90 * math.cos(startAngle * math.pi / 180.0), 90 * math.sin(startAngle * math.pi / 180))
		arc3.lineTo(110 * math.cos(startAngle * math.pi / 180.0), 110 * math.sin(startAngle * math.pi / 180))
		arc3.arcTo(-110, -110, 220, 220, 41, 170)
		arc3.lineTo(90 * math.cos(150 * math.pi / 180.0), 90 * math.sin(150 * math.pi / 180))
		arc3.arcTo(origin.x(), origin.y(), width, height, 210, -170)
		arc3.arcMoveTo(-90, -90, 180, 180, 210)
		arc3.closeSubpath()
		painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
		painter.setBrush(QtGui.QBrush(QtGui.QColor("lime")))
		painter.drawPath(arc3)

		# Write value text
		font = painter.font()
		font.setPixelSize(24)
		painter.setFont(font)

		
		# rect = QtCore.QRect(1, 10, 95, 25)
		# painter.setBrush(QtCore.Qt.black)
		# painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
		# painter.drawRect(1, 10, 95, 25)

		# painter.setPen(QtGui.QPen(QtGui.QColor("lime"), 2))
		# painter.drawText(rect, QtCore.Qt.AlignRight, f"{self.value}")

		# painter.drawText()


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