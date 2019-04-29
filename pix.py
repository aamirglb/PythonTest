import sys
from PySide2 import QtWidgets, QtGui, QtCore

class MyWidget(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.setBackgroundRole(QtGui.QPalette.Dark)
		self.setAutoFillBackground(True)
		self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		self.setFocusPolicy(QtCore.Qt.StrongFocus)
		self.Margin = 20
		# self.setGeometry(0, 0, 400, 300)
		# self.pixmap = QtGui.QPixmap(self.width(), self.height())

		# self.pixmap.fill(QtCore.Qt.white)


	def paintEvent(self, event):
		painter = QtWidgets.QStylePainter(self)
		painter.drawPixmap(0, 0, self.pixmap)
		# painter.setPen(QtCore.Qt.black)
		# painter.drawRect(50, 50, self.width() - 100, self.height() - 100)
		# painter.end()

	def resizeEvent(self, event):
		self.refreshPixmap()

	def refreshPixmap(self):
		self.pixmap = QtGui.QPixmap(self.size())
		# self.pixmap.fill(QtCore.Qt.white)

		painter = QtGui.QPainter(self.pixmap)
		painter.setPen(QtCore.Qt.white)
		doubleMargin = self.Margin * 2
		painter.drawRect(self.Margin, self.Margin, 
			self.width() - doubleMargin, self.height() - doubleMargin)

		painter.setPen(QtCore.Qt.blue)
		painter.drawLine(self.Margin, self.height()/2, self.width() - self.Margin, self.height()/2)
		painter.drawLine(self.width()/2, self.Margin, self.width()/2, self.height() - self.Margin)

		pen = QtGui.QPen(QtCore.Qt.yellow, 1)
		painter.setPen(pen)
		# painter.setPen(QtCore.Qt.white)
		# painter.setPenWidth(4)

		for x in range(self.Margin * 2, self.height(), self.Margin * 2):
			painter.drawLine(self.Margin, x, self.width() - self.Margin, x)
			# painter.drawPoint(self.Margin, x)
			# painter.drawPoint(self.width() - self.Margin, x)
			# painter.drawLine(self.Margin, x)

		
		self.update()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	widget = MyWidget()
	widget.show()

	# pixmap = QtGui.QPixmap(100, 100)
	# pixmap.fill(QtCore.Qt.white)
	# painter = QtGui.QPainter(pixmap)
	# brush = QtGui.QBrush(QtCore.Qt.blue)
	# # painter.setBrush(brush)
	# painter.setPen(QtCore.Qt.blue)
	# painter.drawLine(5, 40, 40, 40)
	# painter.end()

	# label = QtWidgets.QLabel()
	# label.setPixmap(pixmap)
	# label.show()
	sys.exit(app.exec_())

