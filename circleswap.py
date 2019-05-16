import sys
import math
from PySide2 import QtWidgets, QtGui, QtCore

def main():		
	app = QtWidgets.QApplication(sys.argv)
	margin = 10
	scene = QtWidgets.QGraphicsScene(QtCore.QRectF(-200-margin/2, -200-margin/2, 400+margin, 400+margin))
	
	rect = QtWidgets.QGraphicsRectItem(scene.sceneRect().adjusted(1, 1, -1, -1))
	rect.setPen(QtGui.QPen(QtCore.Qt.red, 1))
	# scene.addItem(rect)
	
	radius = 200
	diameter = radius * 2	
	ellipseItem = QtWidgets.QGraphicsEllipseItem(QtCore.QRectF(-200, -200, diameter, diameter))
	ellipseItem.setPen(QtGui.QPen(QtCore.Qt.darkBlue))
	# ellipseItem.setBrush(QtCore.Qt.blue)
	scene.addItem(ellipseItem)	
	
	origin = QtCore.QPointF(0, 0)
	p1 = None
	p2 = None
	angle = 270
	line1 = None
	line2 = None
	conePath = QtGui.QPainterPath()

	def drawLine():
		nonlocal  p1
		nonlocal angle
		nonlocal line1
		nonlocal line2
		nonlocal origin		

		if p1 == None:
			angle2 = angle + 20

			p1 = QtCore.QPointF(radius * math.cos(angle * math.pi / 180.0),
				radius * math.sin(angle * math.pi / 180.0))
			p2 =  QtCore.QPointF(radius * math.cos(angle2 * math.pi / 180.0),
				radius * math.sin(angle2 * math.pi / 180.0))

			line1 = QtWidgets.QGraphicsLineItem(p1.x(), p1.y(), 0, 0)
			line2 = QtWidgets.QGraphicsLineItem(0, 0, p2.x(), p2.y())
			
			# conePath.moveTo(line1)
			# conePath.lineTo(line2)
			# conePath.closeSubpath()
			# scene.addPath(conePath)
			
			scene.addItem(line1)
			scene.addItem(line2)
		else:
			scene.removeItem(line1)
			scene.removeItem(line2)
			# scene.removeItem(conePath)

			angle += 1
			angle2 = angle + 20

			p1 = QtCore.QPointF(radius * math.cos(angle * math.pi / 180.0),
				radius * math.sin(angle * math.pi / 180.0))
			p2 =  QtCore.QPointF(radius * math.cos(angle2 * math.pi / 180.0),
				radius * math.sin(angle2 * math.pi / 180.0))

			line1 = QtWidgets.QGraphicsLineItem(p1.x(), p1.y(), 0, 0)
			line2 = QtWidgets.QGraphicsLineItem(0, 0, p2.x(), p2.y())

			# conePath.moveTo(line1)
			# conePath.lineTo(line2)
			# conePath.closeSubpath()
			# scene.addPath(conePath)

			scene.addItem(line1)
			scene.addItem(line2)		

	view = QtWidgets.QGraphicsView()
	view.setRenderHint(QtGui.QPainter.Antialiasing)
	view.setScene(scene)
	view.show()

	# drawLine()

	timer = QtCore.QTimer()
	timer.setInterval(100)
	timer.timeout.connect(drawLine)
	timer.start()

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
# 