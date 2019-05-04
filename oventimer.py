import sys
import math

from PySide2 import QtWidgets, QtGui, QtCore

class OverTimer(QtWidgets.QWidget):
	DegreesPerMinute = 7.0
	DegreesPerSecond = DegreesPerMinute // 60
	MaxMinutes = 45
	MaxSeconds = MaxMinutes * 60
	UpdateInterval = 5

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
		if secs > 0:
			self.updateTimer.start(self.UpdateInterval * 1000)
			self.finishTimer.start(secs * 1000)
		else:
			updateTimer.stop()
			finishTimer.stop()

	def duration(self):
		secs = QtCore.QDateTime.currentDateTime().secsTo(self.finishTime)
		if secs < 0:
			secs = 0
		return secs
		
	def mousePressEvent(self, event):
		point = QtGui.QPointF(event.pos() - self.rect().center())
		theta = math.atan2(-pint.x(), -point.y()) * 180.0 / math.pi
		self.setDuration(self.duration() + (theta // self.DegreesPerSecond))				
		self.update()

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		painter.setRenderHint(QtGui.QPainter.Antialiasing, True)

		side = min(self.width(), self.height())
		painter.setViewport( (self.width() - side) // 2,
			(self.height() - side) // 2, side, side)
		painter.setWindow(-50, -50, 100, 100)
		self.draw(painter)	 