import sys
from datetime import date
from PySide2 import QtWidgets, QtGui, QtCore

class DaysToGo(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.setWindowTitle('Days To Go')
		self.travelDate = date(2019, 7, 23) # 23rd July 2019
		self.delta = self.travelDate - date.today()
		self.daysRemaining = self.delta.days
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMinMaxButtonsHint)
		# self.setGeometry(10, 900, 90, 110)

	def sizeHint(self):
		return QtCore.QSize(200, 200)

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)

		font = painter.font()
		font.setPointSize(75)
		font.setWeight(QtGui.QFont.Bold)
		painter.setFont(font)

		metrics = QtGui.QFontMetricsF(self.font())
		rect = metrics.boundingRect(f'{self.daysRemaining}');
		rect.translate(-rect.center());


		painter.setPen(QtGui.QPen(QtCore.Qt.black))
		# painter.translate(100, 100)
		painter.drawText(QtCore.QRectF(0, 0, self.width(), self.height()), 
			QtCore.Qt.AlignCenter, f'{self.daysRemaining}')
		# painter.translate(-100, -100)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	widget = DaysToGo()
	widget.show()
	sys.exit(app.exec_())		
