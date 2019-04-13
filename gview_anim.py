from PySide2.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem,
                     QWidget, QGraphicsSimpleTextItem, QGraphicsEllipseItem, QGraphicsPolygonItem, QGraphicsItem,
                     QMenu, QAction)
from PySide2.QtGui import (QPen, QBrush, QPolygonF, QPainter, QFont, QFontMetrics)
from PySide2.QtCore import (Qt, QRectF, QPoint, QPointF, QTimer )

import sys
import random


class MyItem(QGraphicsItem):
    def __init__(self):
        super(MyItem, self).__init__()
        self.angle = random.randint(0, 360)
        self.setRotation(self.angle)
        self.speed = 5

        self.startX = 0
        self.startY = 0

        if random.randint(0, 1) % 1:
            startX = random.randint(0, 200)
            startY = random.randint(0, 200)
        else:
            startX = random.randint(-100, 0)
            startY = random.randint(-100, 0)

        self.setPos(self.mapToParent(startX, startY))           

    def boundingRect(self):
        return QRectF(0, 0, 20, 20)

    def paint(self, painter, option, widget):
        rect = self.boundingRect()
        
        # Collision Detection
        if len(self.scene().collidingItems(self)) < 2 :
            pen = QPen(Qt.green, 5)
            painter.setPen(pen)
        else:
            pen = QPen(Qt.red, 5)
            painter.setPen(pen)
            self.doCollision()

        painter.drawEllipse(rect)                       

    def advance(self, phase):
        if not self.phase:
            return
        location = QPoint(self.pos())
        self.setPos(self.mapToParent(0, -speed))    

    def doCollision(self):
        if random.randint(0, 1) % 1:
            self.setRotation(self.rotation() + (180 + (random.randint(0, 10))))
        else:
            self.setRotation(self.rotation() + (180 + (random.randint(-10, 0))))    
            
        newPoint = QPointF(self.mapToParent(-(self.boundingRect().width()), 
            -(self.boundingRect().width() + 2)))

        if not self.scene().sceneRect().contains((newPoint)):
            print('move to 0, 0')
            newPoint = self.mapToParent(0, 0)
        else:            
            self.setPos(newPoint)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = QGraphicsScene(QRectF(-200, -200, 300, 300))

    view = QGraphicsView()
    view.setRenderHint(QPainter.Antialiasing)
    boundaryPen = QPen(Qt.red)
    scene.addRect(scene.sceneRect())

    itemCount = 20
    for i in range (0, itemCount):
        item = MyItem()
        scene.addItem(item) 

    timer = QTimer()
    timer.setInterval(500)
    timer.timeout.connect(scene.advance)

    view.setScene(scene)
    view.show()
    sys.exit(app.exec_())