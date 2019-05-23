import sys
import math
from PySide2 import QtWidgets, QtCore, QtGui

class Widget(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(Widget, self).__init__(parent)
		self.setBackgroundRole(QtGui.QPalette.Dark)
		self.setAutoFillBackground(True)
		self.w = 400
		self.h = 400
		

	def sizeHint(self):
		return QtCore.QSize(self.w, self.h)

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		w = self.width()
		h = self.height()

		side = min(w, h)
		painter.setViewport((w - side) / 2, (h - side) / 2, side, side)
		painter.setWindow(-w/2, -h/2, w, h)
		painter.setRenderHint(QtGui.QPainter.Antialiasing, True)

		# painter.drawRect(-(w/2-5), -(h/2-5), w-10, h-10)

		# Test
		painter.drawLine(-w/2, 0, w/2, 0)
		painter.drawLine(0, -h/2, 0, h/2)

		painter.drawArc(-100, -100, 200, 200, 0, 16 * 210)

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)

	w = Widget()
	w.show()
	sys.exit(app.exec_())		