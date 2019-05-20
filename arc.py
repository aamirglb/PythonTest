import sys
import math
from PySide2 import QtWidgets, QtCore, QtGui

class Widget(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(Widget, self).__init__(parent)
		self.radius = 100
		self.angle = 0

	def sizeHint(self):
		return QtCore.QSize(400, 400)

	@QtCore.Slot(int)
	def setValue(self, _angle):
		self.angle = _angle % 360
		self.update()

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		painter.setWindow(-200, -200, 400, 400)
		painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
		painter.drawRect(-195, -195, 390, 390)

		# Test
		painter.drawLine(-200, 0, 200, 0)
		painter.drawLine(0, -200, 0, 200)
		
		painter.save()		
		# make counter clockwise from 3 o'clock
		painter.rotate(360 - self.angle)
		painter.drawLine(0, 0, self.radius, 0)
		painter.setBrush(QtCore.Qt.red)
		painter.drawEllipse(self.radius-5, -5, 10, 10)
		
		painter.restore()

		painter.drawArc(-100, -100, 100*2, 100*2, 0, 16 * self.angle)
		painter.drawArc(-20, -20, 20*2, 20*2, 0, 16 * self.angle)
		painter.drawText(21, -21, f'{self.angle}')

	value = QtCore.Property(int, fset=setValue)

def animationFinished():	
	animation.setStartValue(0)
	animation.setEndValue(360)		
	animation.start()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)

	w = Widget()
	animation = QtCore.QPropertyAnimation(w, b"value")
	animation.setDuration(3600*2)
	animation.setStartValue(0)
	animation.setEndValue(360)
	animation.finished.connect(animationFinished)
	animation.start()

	w.show()
	sys.exit(app.exec_())


