from PySide2.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem,
                     QWidget, QGraphicsSimpleTextItem, QGraphicsEllipseItem, QGraphicsPolygonItem, QGraphicsItem,
                     QMenu, QAction)
from PySide2.QtGui import (QPen, QBrush, QPolygonF, QPainter, QFont, QFontMetrics)
from PySide2.QtCore import (Qt, QRectF, QPoint, QPointF, QTimer )

import sys

class TimeElapsedTape(QGraphicsItem):
    def __init__(self, parent=None):
        super(TimeElapsedTape, self).__init__(parent)
        # time in seconds
        self.currTime = 0
        self.width = 800
        self.height = 50
        self.lineDistance = 10

    def boundingRect(self):           
        return QRectF(0, 0, self.width, self.height+20)

    def setCurTime(self, sec):
        self.currTime = sec
        self.update()

    def paint(self, painter, option, widget):
        rect = self.boundingRect()
        brush = QBrush()
        brush.setStyle(Qt.SolidPattern)
        brush.setColor(Qt.lightGray)
        painter.setBrush(brush)
        painter.drawRect(QRectF(0, 0, self.width, self.height))

        painter.setPen(QPen(Qt.red, 2))
        painter.drawLine(QPointF(self.width/2, 0), QPointF(self.width/2, self.height))
        
        font = painter.font()
        font.setPixelSize(12)
        font.setWeight(QFont.Bold)
        fontMetrics = QFontMetrics(font)
        painter.setFont(font)
        textRect = fontMetrics.boundingRect(str(self.currTime))
        painter.drawText(self.width/2 - (textRect.width()/2), 65, str(self.currTime))        
        painter.setPen(QPen(Qt.black, 1))
        
        # one line after 5 pixels
        startValue = self.currTime        
        origin = (self.width / 2) - (startValue * self.lineDistance)
        min = int(startValue - (self.width * .5) / self.lineDistance)
        max = int(startValue + (self.width * .5) / self.lineDistance)
        
        for i in range(min, max):
            x1 = x2 = origin + (i * self.lineDistance)
            y1 = self.height
             
            if i % 10 == 0:
                y2 = 10
                if i >= 0:                 
                    font.setWeight(QFont.Bold)
                    font.setPixelSize(10)
                    painter.setFont(font)
                    painter.drawText(x1, 10, f'{i}')
            elif i % 5 == 0:
                y2 = 25
            else:
                y2 = 37
            if i >= 0:                 
                painter.drawLine(x1, y1, x2, y2)            

def timerHandler(): 
    tape.setCurTime(tape.currTime+1)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = QGraphicsScene(QRectF(-10, -100, 850, 250))
    # scene.addItem(QGraphicsRectItem(scene.sceneRect()))
    
    tape = TimeElapsedTape()
    scene.addItem(tape)

    timer = QTimer()
    timer.setInterval(1000)
    timer.timeout.connect(timerHandler)

    view = QGraphicsView()
    view.setScene(scene)
    view.show()
    timer.start()   
    sys.exit(app.exec_())           