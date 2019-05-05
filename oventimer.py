import sys
import math

from PySide2 import QtWidgets, QtGui, QtCore

class OvenTimer(QtWidgets.QWidget):
	DegreesPerMinute = 7.0 
	DegreesPerSecond = DegreesPerMinute / 60 
	MaxMinutes = 45
	MaxSeconds = MaxMinutes * 60
	UpdateInterval = 5
	timeout = QtCore.Signal()

	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.finishTime = QtCore.QDateTime.currentDateTime()
		self.updateTimer = QtCore.QTimer(self)
		self.updateTimer.timeout.connect(self.update)

		self.finishTimer = QtCore.QTimer(self)
		self.finishTimer.setSingleShot(True)
		self.finishTimer.timeout.connect(self.timeout)
		self.finishTimer.timeout.connect(self.updateTimer.stop)

		font = QtGui.QFont()
		font.setPointSize(9)
		self.setFont(font)

	def setDuration(self, secs):
		if secs < 0:
			secs = 0
		elif secs > self.MaxSeconds:
			secs = self.MaxSeconds

		self.finishTime = QtCore.QDateTime.currentDateTime().addSecs(secs)
		# self.finishTime = QtCore.QDateTime.currentDateTime().addMSecs(secs)
		if secs > 0:
			self.updateTimer.start(self.UpdateInterval * 1000)
			self.finishTimer.start(secs * 1000)
		else:
			self.updateTimer.stop()
			self.finishTimer.stop()

	def duration(self):
		secs = QtCore.QDateTime.currentDateTime().secsTo(self.finishTime)
		if secs < 0:
			secs = 0
		return secs
		
	def mousePressEvent(self, event):
		point = QtCore.QPointF(event.pos() - self.rect().center())
		theta = math.atan2(-point.x(), -point.y()) * 180.0 / math.pi
		print(f'Duration: {self.duration() + (theta / self.DegreesPerSecond)}')
		self.setDuration(self.duration() + (theta / self.DegreesPerSecond))				
		self.update()

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		painter.setRenderHint(QtGui.QPainter.Antialiasing, True)

		side = min(self.width(), self.height())
		painter.setViewport( (self.width() - side) // 2,
			(self.height() - side) // 2, side, side)
		painter.setWindow(-50, -50, 100, 100)
		self.draw(painter)	 

	def draw(self, painter):
		triangle = [QtCore.QPoint(-2, -49), QtCore.QPoint(+2, -49), 
		QtCore.QPoint(0, -47)]
		thickPen = QtGui.QPen(self.palette().foreground(), 1.5)
		thinPen = QtGui.QPen(self.palette().foreground(), 0.5)
		niceBlue = QtGui.QColor(150, 150, 200)

		painter.setPen(thinPen)
		painter.setBrush(self.palette().foreground())
		painter.drawPolygon(QtGui.QPolygon(triangle))

		coneGradient = QtGui.QConicalGradient(0, 0, -90.0)
		coneGradient.setColorAt(0.0, QtCore.Qt.darkGray)
		coneGradient.setColorAt(0.2, niceBlue)
		coneGradient.setColorAt(0.5, QtCore.Qt.white)
		coneGradient.setColorAt(1.0, QtCore.Qt.darkGray)

		painter.setBrush(coneGradient)
		painter.drawEllipse(-46, -46, 92, 92)

		haloGradient = QtGui.QRadialGradient(0, 0, 20, 0, 0)
		haloGradient.setColorAt(0.0, QtCore.Qt.lightGray)
		haloGradient.setColorAt(0.8, QtCore.Qt.darkGray)
		haloGradient.setColorAt(0.9, QtCore.Qt.white)
		haloGradient.setColorAt(1.0, QtCore.Qt.black)

		painter.setPen(QtCore.Qt.NoPen)
		painter.setBrush(haloGradient)
		painter.drawEllipse(-20, -20, 40, 40)

		knobGradient = QtGui.QLinearGradient(-7, -25, 7, -25)
		knobGradient.setColorAt(0.0, QtCore.Qt.black)
		knobGradient.setColorAt(0.2, niceBlue)
		knobGradient.setColorAt(0.3, QtCore.Qt.lightGray)
		knobGradient.setColorAt(0.8, QtCore.Qt.white)
		knobGradient.setColorAt(1.0, QtCore.Qt.black)

		painter.rotate(self.duration() * self.DegreesPerSecond)
		painter.setBrush(knobGradient)
		painter.setPen(thinPen)
		painter.drawRoundRect(-7, -25, 14, 50, 99, 49)

		for i in range(0, self.MaxMinutes+1):
			painter.save()
			painter.rotate(-i * self.DegreesPerMinute)

			if i % 5 == 0:
				painter.setPen(thickPen)
				painter.drawLine(0, -41, 0, -44)
				painter.drawText(-15, -41, 30, 30, 
					QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop,
					str(i))
			else:
				painter.setPen(thinPen)
				painter.drawLine(0, -42, 0, -44)
			painter.restore()

			# if i % 5 == 0:
			# 	painter.setPen(thickPen)
			# 	painter.drawLine(0, -41, 0, -44)
			# 	painter.drawText(-15, -41, 30, 30, 
			# 		QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop,
			# 		str(i))
			# else:
			# 	painter.setPen(thinPen)
			# 	painter.drawLine(0, -42, 0, -44)
			# painter.rotate(-self.DegreesPerMinute)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)

	ovenTimer = OvenTimer()
	ovenTimer.show()

	sys.exit(app.exec_())
