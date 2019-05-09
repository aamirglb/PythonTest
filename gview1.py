from PySide2.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem,
	                 QWidget, QGraphicsSimpleTextItem, QGraphicsEllipseItem, QGraphicsPolygonItem,
	                 )
from PySide2.QtGui import (QPen, QBrush, QPolygonF)
from PySide2.QtCore import (Qt, QRectF, QPoint, QPointF )

import sys

if __name__ == '__main__':
	app = QApplication(sys.argv)
	scene = QGraphicsScene(QRectF(-50, -50, 400, 200))
	
	rect = QGraphicsRectItem(scene.sceneRect().adjusted(1, 1, -1, -1))
	rect.setPen(QPen(Qt.red, 1))
	scene.addItem(rect)
	
	rectItem = QGraphicsRectItem(QRectF(-25, 25, 200, 40))
	rectItem.setPen(QPen(Qt.red, 3, Qt.DashDotLine))
	rectItem.setBrush(Qt.gray)
	scene.addItem(rectItem)
	print(f'Rect Pos: {rectItem.pos()}')

	textItem = QGraphicsSimpleTextItem("Foundation of Qt")
	scene.addItem(textItem)
	print(f'Text Pos: {textItem.pos()}')
	textItem.setPos(50, 0)
	print(f'Text Pos: {textItem.pos()}')

	ellipseItem = QGraphicsEllipseItem(QRectF(170, 20, 100, 75))
	ellipseItem.setPen(QPen(Qt.darkBlue))
	ellipseItem.setBrush(Qt.blue)
	scene.addItem(ellipseItem)

	points = [QPointF(10, 10), QPointF(0, 90), QPointF(40, 70), QPointF(80, 110),
	QPointF(70, 20)]

	polygonItem = QGraphicsPolygonItem(QPolygonF(points))
	polygonItem.setPen(QPen(Qt.darkGreen))
	polygonItem.setBrush(Qt.yellow)
	scene.addItem(polygonItem)

	view = QGraphicsView()
	view.setScene(scene)
	view.show()

	sys.exit(app.exec_())