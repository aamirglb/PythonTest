import sys
import random
from PySide2 import QtWidgets, QtGui, QtCore

class Battery(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(Battery, self).__init__(parent)
		self.value = -1
		self.visible = True
		self.timer = QtCore.QTimer()
		self.timer.setInterval(500)
		self.timer.timeout.connect(self.blink)

	def sizeHint(self):
		return QtCore.QSize(36, 18)

	def minimumSizeHint(self):
		return QtCore.QSize(36, 18)

	def blink(self):
		if self.visible:
			self.visible = False
		else:
			self.visible = True
		self.update()

	def paintEvent(self, evnet):
		if not self.visible:
			return

		painter = QtGui.QPainter(self)
		painter.setRenderHint(QtGui.QPainter.Antialiasing)		

		path = QtGui.QPainterPath()
		path.addRoundedRect(QtCore.QRectF(2, 1, 30, 16), 3, 3)
		path.addRoundedRect(QtCore.QRectF(32, 5, 3, 8), 2, 2)
		painter.drawPath(path)

		# depending on value set the fill pattern
		# 100% charged correspond to fill width of 30 px
		w = (self.value * 29) // 100
		color = QtCore.Qt.red
		if self.value > 25:
			color = QtGui.QColor("lime")
		elif self.value > 10:
			color = QtGui.QColor("orange")
		else:
			color = QtGui.QColor("red")
		
		painter.save()
		painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
		painter.setBrush(QtGui.QBrush(color))
		painter.drawRect(QtCore.QRectF(3, 2, w, 14))
		painter.restore()

		font = painter.font()
		font.setBold(True)
		font.setPixelSize(8)
		painter.setFont(font)		

		painter.drawText(4, 12, f"{self.value}%")


	@QtCore.Slot(int)
	def setValue(self, _val):
		if self.value != _val:			
			self.value = _val
			self.update()

			if self.value <= 10:
				self.timer.start()
			else:
				self.visible = True
				self.timer.stop()	 


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)

	count = 3
	b = [None] * count
	s = [None] * count
	layout = QtWidgets.QGridLayout()

	for i in range(0, count):
		b[i] = Battery()
		s[i] = QtWidgets.QSlider(QtCore.Qt.Horizontal)
		s[i].setRange(0, 100)		
		s[i].valueChanged.connect(b[i].setValue)
		s[i].setValue(random.randint(0, 100))
		layout.addWidget(b[i], i, 0, 1, 1)
		layout.addWidget(s[i], i, 1, 1, 2)

	window = QtWidgets.QWidget()
	window.setLayout(layout)
	window.show()

	app.exec_()	