import sys
from PySide2 import QtWidgets, QtGui, QtCore

class MyWidget(QtWidgets.QWidget):
	def __init__(self, w, h, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.setWindowTitle('Viewport Test')
		self.rotation = 0
		self.width = w
		self.height = h
		self.timer = QtCore.QTimer()
		self.timer.setInterval(10)
		self.timer.timeout.connect(lambda : self.update())
		self.timer.start()

	def sizeHint(self):
		return QtCore.QSize(self.width, self.height)

	def paintEvent(self, event):
		
		painter = QtGui.QPainter(self)
		# These gets mapped always to self.width() & self.height()
		painter.setWindow(-self.width/2, -self.height/2, self.width, self.height)
		
		if False:			
			transform = QtGui.QTransform()
			transform.translate(-self.width/4, -self.height/4);
			transform.rotate(self.rotation)
			transform.translate(self.width/4, self.height/4);
			painter.setWorldTransform(transform)
		else:
			# Use QPainter function instead of world transformation	
			painter.translate(-self.width/4, -self.height/4);
			painter.rotate(self.rotation)
			painter.translate(self.width/4, self.height/4);
			
		self.rotation += 1
		if self.rotation > 360:
			self.rotation = 0

		

		w = self.width/4
		h = self.height/4

		painter.drawRect(0, 0, w, h)
		painter.setPen(QtGui.QPen(QtCore.Qt.red, 3))
		painter.drawRect(-w, -h, w, h)
		painter.setPen(QtGui.QPen(QtCore.Qt.blue, 3))
		painter.drawRect(-w, 0, w, h)
		painter.setPen(QtGui.QPen(QtCore.Qt.darkGreen, 3))
		painter.drawRect(0, -h, w, h)

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	widget = MyWidget(600, 600)
	widget.show()
	
	sys.exit(app.exec_())
