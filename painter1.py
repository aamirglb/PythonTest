import sys
from PySide2 import QtWidgets, QtGui, QtCore

class MyWidget(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.setWindowTitle('Painter Test')

	def paintEvent(self, event):
		penCapStyle = [QtCore.Qt.FlatCap, QtCore.Qt.SquareCap, QtCore.Qt.RoundCap]
		penJoinStyle = [QtCore.Qt.MiterJoin, QtCore.Qt.BevelJoin, QtCore.Qt.RoundJoin]

		brushStyle = [QtCore.Qt.SolidPattern, QtCore.Qt.Dense1Pattern, 
		QtCore.Qt.Dense7Pattern, QtCore.Qt.CrossPattern, 
		QtCore.Qt.FDiagPattern, QtCore.Qt.DiagCrossPattern]

		painter = QtGui.QPainter(self)
		painter.setRenderHint(QtGui.QPainter.Antialiasing, True)

		painter.setPen(QtGui.QPen(QtCore.Qt.black, 15, QtCore.Qt.SolidLine, 
			QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
		painter.setBrush(QtGui.QBrush(QtCore.Qt.blue, QtCore.Qt.DiagCrossPattern))
		# painter.drawPie(80, 80, 400, 240, 60 * 16, 270 * 16)

		poly = [QtCore.QPoint(0, 85), QtCore.QPoint(75, 75), QtCore.QPoint(100, 10), 
		        QtCore.QPoint(125, 75), QtCore.QPoint(200, 85), QtCore.QPoint(150, 125), 
		        QtCore.QPoint(160, 190), QtCore.QPoint(100, 150), QtCore.QPoint(40, 190), 
		        QtCore.QPoint(50, 125), QtCore.QPoint(0, 85)]

		gradient = QtGui.QLinearGradient(50, 100, 300, 350)
		gradient.setColorAt(0.0, QtCore.Qt.white)
		gradient.setColorAt(0.5, QtCore.Qt.green)
		gradient.setColorAt(1.0, QtCore.Qt.black)
		painter.setBrush(gradient)
		painter.setBackgroundColor(QtCore.Qt.red)
		painter.setPen(QtGui.QPen(QtCore.Qt.red, 4, QtCore.Qt.DashDotLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
		# painter.drawPolygon(poly)
		painter.drawRect(80, 80, 240, 140)

		# path = QtGui.QPainterPath()
		# path.moveTo(80, 320)
		# path.cubicTo(200, 80, 320, 80, 480, 320)
		# painter.setPen(QtGui.QPen(QtCore.Qt.black, 8))
		# painter.drawPath(path)

		# for i in range(0, 3):
		# 	painter.setPen(QtGui.QPen(QtCore.Qt.black, 12, 
		# 	QtCore.Qt.DashDotLine, penCapStyle[i], penJoinStyle[i]))
		# 	painter.setBrush(QtGui.QBrush(QtCore.Qt.green, brushStyle[i]))

		# 	if i < 3:
		# 		x = 50 + (200 * i)
		# 		y = 10
		# 	else:
		# 		x = 50 + (200 * (i-3))
		# 		y = 200
		# 	print(f'({x}, {y})')
		# 	painter.drawEllipse(x, y, 200, 100)
			


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	widget = MyWidget()
	widget.show()
	sys.exit(app.exec_())