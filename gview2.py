from PySide2.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem,
	                 QWidget, QGraphicsSimpleTextItem, QGraphicsEllipseItem, QGraphicsPolygonItem, QGraphicsItem
	                 )
from PySide2.QtGui import (QPen, QBrush, QPolygonF)
from PySide2.QtCore import (Qt, QRectF, QPoint, QPointF, QTimer )

import sys

def createItem(x, scene):
	rectItem = QGraphicsRectItem(QRectF(x+40, 40, 120, 120))
	scene.addItem(rectItem)
	rectItem.setPen(QPen(Qt.black))
	rectItem.setBrush(Qt.gray)

	innerRectItem = QGraphicsRectItem(QRectF(x+50, 50, 45, 100), rectItem)
	innerRectItem.setPen(QPen(Qt.black))
	innerRectItem.setBrush(Qt.white)
	# scene.addItem(innerRectItem)

	ellipseItem = QGraphicsEllipseItem(QRectF(x+105, 50, 45, 100), rectItem)
	ellipseItem.setPen(QPen(Qt.black))
	ellipseItem.setBrush(Qt.white)
	# scene.addItem(ellipseItem)
	return rectItem

def timerHandler():
	global sec
	item2.setTransformOriginPoint(300, 100)
	item2.setRotation(sec)
	sec += 1

if __name__ == '__main__':
	app = QApplication(sys.argv)
	scene = QGraphicsScene(QRectF(0, 0, 1000, 200))
	scene.addItem(QGraphicsRectItem(scene.sceneRect()))

	item1 = createItem(0, scene)
	sec = 0
	item2 = createItem(200, scene)

	timer = QTimer()
	timer.setInterval(1000)
	timer.timeout.connect(timerHandler)
	# item2.mapToScene(300, 100)
	# # item2.translate(300, 100)
	item2.setTransformOriginPoint(300, 100)
	item2.setRotation(30)
	# # item2.translate(-300, -100)
	# item2.mapToScene(-300, -100)

	item3 = createItem(400, scene)
	# item3.translate(500, 100)
	item3.setTransformOriginPoint(500, 100)
	item3.setScale(0.5)
	# item3.translate(-500, -100)

	# item4 = createItem(600, scene)
	# item4.translate(700, 100)
	# item4.shear(0.1, 0.3)
	# item4.translate(-700, -100)

	# item5 = createItem(800, scene)
	# item5.translate(900, 100)
	# item5.scale(0.5, 0.7)
	# item5.rotate(30)
	# item5.shear(0.1, 0.3)
	# item5.translate(-900, -100)

	view = QGraphicsView()
	view.setScene(scene)
	view.show()
	# timer.start()
	sys.exit(app.exec_())