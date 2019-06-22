import sys
import math
from PySide2 import QtWidgets, QtGui, QtCore

LevelTriangle = [QtCore.QPointF(-5.0, -95.0),
                 QtCore.QPointF(+5.0, -95.0),
                 QtCore.QPointF( 0.0, -90.0)]

BankTriangle = [QtCore.QPointF(-10.0, -85.0),
		        QtCore.QPointF(+10.0, -85.0),
		        QtCore.QPointF(  0.0, -90.0)]                  

BankMarkAngles = [10, 20, 30, 45, 60]

AvMarker = [QtCore.QPointF(-30.0, +5.0),
		    QtCore.QPointF(+30.0, +5.0),
		    QtCore.QPointF(  0.0,  0.0)]

Boarder = [QtCore.QPointF(-180.0, -112.0),
		   QtCore.QPointF(+180.0, -112.0),
		   QtCore.QPointF(+180.0, +112.0),
		   QtCore.QPointF(-180.0, +112.0)]

class Efis(QtWidgets.QWidget):
	
	def __init__(self, parent=None):
		super(Efis, self).__init__(parent)
		self.pitch = 0
		self.bank = 0
		self.setGeometry(QtCore.QRect(140, 256, 360, 224))
		self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		painter.setRenderHint(QtGui.QPainter.Antialiasing, True)

		painter.setWindow(-180, -112, 360, 224)
		self.drawEarth(painter)
		self.drawPitchMarkers(painter)
		self.drawBankMarkers(painter)
		self.drawPlaneBank(painter)

		pen = QtGui.QPen()
		pen.setColor(QtCore.Qt.black)
		pen.setJoinStyle(QtCore.Qt.RoundJoin)
		pen.setWidth(1)
		painter.setPen(pen)

		painter.drawPolygon(Boarder)

		pen.setColor(QtCore.Qt.yellow)
		painter.setPen(pen)
		painter.drawPolygon(AvMarker)

	def drawEarth(self, painter):
		painter.save()
		painter.rotate(-self.bank)

		skyHeight = 400 + (self.pitch * 3)
		skyEndY = -400 + skyHeight

		skyGradient = QtGui.QLinearGradient(0, -270, 0, skyEndY + 20)
		skyGradient.setColorAt(0, QtGui.QColor(24, 90, 206, 255))
		skyGradient.setColorAt(1, QtCore.Qt.white)
		painter.fillRect(-300, -300, 600, skyHeight, skyGradient)

		groundHeight = 270 + 30 - (self.pitch * 3)
		groundGradient = QtGui.QLinearGradient(0, 270, 0, skyEndY - 60)
		groundGradient.setColorAt(0, QtGui.QColor(180, 130, 30, 255))
		groundGradient.setColorAt(1, QtCore.Qt.white)
		painter.fillRect(-300, 300, 600, -groundHeight, groundGradient)

		painter.restore()

	def drawPitchMarkers(self, painter):
		painter.save()

		brush = QtGui.QBrush(QtCore.Qt.black)
		painter.setBrush(brush)

		font = QtGui.QFont(painter.font())
		font.setPixelSize(10)
		painter.setFont(font)

		pen = QtGui.QPen(painter.pen())
		pen.setColor(QtCore.Qt.black)
		painter.setPen(pen)

		painter.drawRoundRect(-20, -1, -50, 1, 2, 5)
		painter.drawRoundRect(+20, -1, +50, 1, 2, 5)

		painter.rotate(-self.bank)

		step = 0
		for i in range(5, 45, 5):			
			painter.translate(0, 10)
			step += 10
			if i % 10 == 0:
				painter.drawRoundRect(-15, -1, 30, 1, 2, 5)
				painter.setPen(QtGui.QPen(QtCore.Qt.black))
				painter.drawText(QtCore.QRect(20, -5, 50, 10),
					QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, f'{self.pitch - i}')
			else:
				painter.drawRoundRect(-10, -1, 20, 1, 2, 5)
		painter.translate(0, -step)
		
		step = 0
		for i in range(0, 35, 5):
			# if step < -45:
			# 	print(f'breaking when i = {i}, step = {step}')
			# 	break

			painter.translate(0, -10)
			step -= 10			

			if i % 10 == 0:
				painter.drawRoundRect(-15, -1, 30, 1, 2, 5)
				painter.setPen(QtGui.QPen(QtCore.Qt.black))
				painter.drawText(QtCore.QRect(20, -5, 50, 10),
					QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, f'{self.pitch + i}')			
			else:
				painter.drawRoundedRect(-10, -1, 20, 1, 2, 5)

		painter.restore()				

	def drawBankMarkers(self, painter):
		painter.save()

		pen = QtGui.QPen(painter.pen())
		pen.setColor(QtCore.Qt.black)
		pen.setJoinStyle(QtCore.Qt.RoundJoin)
		pen.setCapStyle(QtCore.Qt.RoundCap)
		pen.setWidth(1)
		painter.setPen(pen)

		painter.drawPolygon(LevelTriangle)

		for i in range(0, 5):
			angle = BankMarkAngles[i]
			painter.rotate(-angle)

			if angle == 45:
				painter.drawPolygon(LevelTriangle)
			else:
				painter.drawLine(0, -95, 0, -90)

			painter.drawText(QtCore.QRect(0, -110, 20, 10),
					QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, f'{(i*5)}')	
			painter.rotate(angle)	

		for i in range(0, 5):
			angle = BankMarkAngles[i]
			painter.rotate(angle)
			if angle == 45:
				painter.drawPolygon(LevelTriangle)
			else:
				painter.drawLine(0, -95, 0, -90)
			painter.rotate(-angle)
		
		painter.restore()		

	def drawPlaneBank(self, painter):
		painter.save()

		painter.setBrush(QtGui.QBrush(QtCore.Qt.black))
		pen = QtGui.QPen(painter.pen())
		pen.setColor(QtCore.Qt.yellow)
		pen.setJoinStyle(QtCore.Qt.RoundJoin)
		pen.setWidth(1)
		painter.setPen(pen)

		painter.rotate(-self.bank)
		painter.drawPolygon(BankTriangle)
		painter.restore()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)

	efis = Efis()
	efis.show()

	sys.exit(app.exec_())

