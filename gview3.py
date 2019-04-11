from PySide2.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem,
	                 QWidget, QGraphicsSimpleTextItem, QGraphicsEllipseItem, QGraphicsPolygonItem, QGraphicsItem,
	                 QMenu, QAction)
from PySide2.QtGui import (QPen, QBrush, QPolygonF, QPainter, QFont, )
from PySide2.QtCore import (Qt, QRectF, QPoint, QPointF, QTimer )

import sys

class SlotItem(QGraphicsItem):
    def __init__(self, id, parent=None):
    	super(SlotItem, self).__init__(parent)
    	self.width = 100
    	self.height = 70
    	self.id = id

    def boundingRect(self):           
        return QRectF(0, 0, self.width, self.height)

    def paint(self, painter, option, widget):
     	rect = self.boundingRect()
     	painter.drawRect(rect)
     	font = painter.font()
     	font.setPixelSize(12)
     	font.setWeight(QFont.Bold)
     	painter.setFont(font)
     	painter.drawText((self.width/2)-4, 15, f'{self.id}')

    def contextMenuEvent(self, event):
        self.menu = QMenu()
        self.showModeAction = QAction(f'Slot {self.id}')
        self.menu.addAction(self.showModeAction)
        self.menu.exec_(event.screenPos())

class BracketItem(QGraphicsItem):
    def __init__(self, id):
        super(BracketItem, self).__init__()
        self.zoomFactor = 1
        self.rootSlot = SlotItem(1, self)
        self.leftChild = SlotItem(2, self)
        self.rightChild = SlotItem(3, self)

        self.rootSlot.setPos(120, 20)
        self.leftChild.setPos(20, 140)
        self.rightChild.setPos(220, 140)

        self.scaleFactor = 1


    def boundingRect(self):
        return QRectF(0, 0, 340, 230)

    def paint(self, painter, option, widget):
        # self.scaleFactor -= 0.1
        # painter.scale(self.scaleFactor, self.scaleFactor)
        rect = self.boundingRect()
        painter.drawRect(rect)
        painter.drawLine(170, 90, 70, 140)
        painter.drawLine(170, 90, 270, 140)


    def contextMenuEvent(self, event):
        self.menu = QMenu()
        self.showModeAction = QAction('Bracket')
        self.menu.addAction(self.showModeAction)
        self.menu.exec_(event.screenPos())

def timerHandler():	
	bracket1.scaleFactor -= 0.1
	print(f'scaleFactor: {bracket1.scaleFactor}')
	bracket1.setScale(bracket1.scaleFactor)
	if bracket1.scaleFactor < 0.5:
		timer.stop()
	

if __name__ == '__main__':
	app = QApplication(sys.argv)
	scene = QGraphicsScene(QRectF(-50, -50, 500, 400))
	# scene.addItem(QGraphicsRectItem(scene.sceneRect()))
	
	bracket1 = BracketItem(1)
	scene.addItem(bracket1)

	timer = QTimer()
	timer.setInterval(7000)
	timer.timeout.connect(timerHandler)

	view = QGraphicsView()
	view.setScene(scene)
	view.show()
	timer.start()	
	sys.exit(app.exec_())     