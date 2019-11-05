# from PySide2.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem,
# 	                 QWidget, QGraphicsSimpleTextItem, QGraphicsEllipseItem, QGraphicsPolygonItem,
# 	                 )
# from PySide2.QtGui import (QPen, QBrush, QPolygonF)
# from PySide2.QtCore import (Qt, QRectF, QPoint, QPointF, QTimer)

import sys
from PySide2 import QtWidgets, QtGui, QtCore


class FanBlade(QtWidgets.QGraphicsItem):
    def __init__(self, angle = 0, parent=None):
        super(FanBlade, self).__init__(parent)
        # time in seconds
        self.angle = angle
        self.width = 80
        self.height = 20
        self.setFlag(QtWidgets.QGraphicsItem.ItemIgnoresTransformations, True);

    def boundingRect(self):           
        return QtCore.QRectF(0, 0, self.width+2, self.height+2)        

    def setAngle(self, angle):
    	self.angle = angle 
    	self.update()   	

    def paint(self, painter, option, widget):
        rect = self.boundingRect()
        painter.setPen(QtGui.QPen(QtCore.Qt.darkBlue))
        painter.setBrush(QtCore.Qt.yellow)
        painter.rotate(self.angle)
        # painter.drawRect(QRectF(0, 0, self.width, self.height))
        # painter.drawEllipse(QtCore.QRectF(-10, -10, 80, 20))
        myPath = QtGui.QPainterPath()
        myPath.moveTo(QtCore.QPoint(scene.sceneRect().width()/2, 0))
        myPath.arcTo(QtCore.QRectF(50, -25, 50, 50), 0, -90)
        myPath.arcTo(QtCore.QRectF(0, -12.5, 25, 25), 270, -180)	
        myPath.arcTo(QtCore.QRectF(50, -25, 50, 50), 90, -90)
        myPath.closeSubpath()
        painter.drawPath(myPath)
        

def timerHandler(): 
    increment = 15
    blade1.setAngle(blade1.angle+increment)
    blade2.setAngle(blade2.angle+increment)
    blade3.setAngle(blade3.angle+increment)    
    view.viewport().repaint()

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	scene = QtWidgets.QGraphicsScene(QtCore.QRectF(-100, -100, 200, 200))
	scene.addItem(QtWidgets.QGraphicsRectItem(scene.sceneRect()))	

	centerItem = QtWidgets.QGraphicsEllipseItem(QtCore.QRectF(-10, -10, 20, 20))	
	centerItem.setPen(QtGui.QPen(QtCore.Qt.darkBlue))
	centerItem.setBrush(QtCore.Qt.green)
	centerItem.setZValue(2)
	scene.addItem(centerItem)

	circle1 = QtWidgets.QGraphicsEllipseItem(QtCore.QRectF(-75, -75, 150, 150))
	circle1.setPen(QtGui.QPen(QtCore.Qt.black))
	circle1.setBrush(QtCore.Qt.NoBrush)
	# scene.addItem(circle1)

	blade1 = FanBlade()	
	scene.addItem(blade1)

	blade2 = FanBlade(120)
	scene.addItem(blade2)

	blade3 = FanBlade(240)
	scene.addItem(blade3)

	timer = QtCore.QTimer()
	timer.setInterval(250)
	timer.timeout.connect(timerHandler)	
	timer.start()

	# myPath = QtGui.QPainterPath()
	# myPath.moveTo(QtCore.QPoint(scene.sceneRect().width()/2, 0))
	# myPath.arcTo(QtCore.QRectF(50, -25, 50, 50), 0, -90)
	# myPath.arcTo(QtCore.QRectF(-100, -12.5, 25, 25), 270, -180)
	# # myPath.arcTo(QtCore.QRectF(-100, -12.5, 25, 25), 180, -10)
	# myPath.arcTo(QtCore.QRectF(50, -25, 50, 50), 90, -90)
	# # myPath.arcTo(scene.sceneRect(), 0, -20)
	
	# # myPath.arcTo(scene.sceneRect(), 190, -20)
	# # myPath.arcTo(scene.sceneRect(), 20, -20)
	# # myPath.closeSubpath()
	# scene.addPath(myPath)

	view = QtWidgets.QGraphicsView()
	view.setScene(scene)
	view.show()
	
	sys.exit(app.exec_())
