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
        self.width = 400
        self.height = 50
        self.lineSpacing = 5
        self.direction = 1 # Horizontal
        
        self.backColor = Qt.black        
        self.linePen = QPen(Qt.white, 1)
        self.textPen = QPen(Qt.white, 1)

        self.backColor = Qt.lightGray        
        self.linePen = QPen(Qt.black, 1)
        self.textPen = QPen(Qt.black, 1)

        self.backColor = Qt.blue        
        self.linePen = QPen(Qt.white, 1)
        self.textPen = QPen(Qt.white, 1)

        self.width, self.height = self.height, self.width

    def boundingRect(self):           
        return QRectF(0, 0, self.width+20, self.height)

    def setCurTime(self, sec):
        self.currTime = sec
        self.update()

    def paint(self, painter, option, widget):
        rect = self.boundingRect()
        brush = QBrush()
        brush.setStyle(Qt.SolidPattern)
        brush.setColor(self.backColor)
        painter.setBrush(brush)
        painter.drawRect(QRectF(0, 0, self.width, self.height))

        painter.setPen(QPen(Qt.red, 2))
        # painter.drawLine(QPointF(self.width/2, 0), QPointF(self.width/2, self.height))

        painter.drawLine(QPointF(0, self.height/2), QPointF(self.width, self.height/2))
        
        font = painter.font()
        font.setPixelSize(12)
        font.setWeight(QFont.Bold)
        fontMetrics = QFontMetrics(font)
        painter.setFont(font)
        textRect = fontMetrics.boundingRect(str(self.currTime))
        painter.drawText(QPointF(50+5, self.height/2), str(self.currTime))       
        painter.setPen(self.linePen)
        
        # one line after 5 pixels
        startValue = self.currTime        
        # origin = (self.width / 2) - (startValue * self.lineSpacing)
        # min = int(startValue - (self.width * .5) / self.lineSpacing)
        # max = int(startValue + (self.width * .5) / self.lineSpacing)

        origin = (self.height / 2) - (startValue * self.lineSpacing)
        min = int(startValue - (self.height * .5) / self.lineSpacing)
        max = int(startValue + (self.height * .5) / self.lineSpacing)
        
        for i in range(min, max):
            # x1 = x2 = origin + (i * self.lineSpacing)
            # y1 = self.height

            x1 = self.width
            y1 = y2 = origin + (i * self.lineSpacing)
             
            if i % 10 == 0:
                x2 = 10
                if i >= 0:                 
                    font.setWeight(QFont.Bold)
                    font.setPixelSize(10)
                    painter.setFont(font)
                    painter.drawText(0, y1, f'{i}')
            elif i % 5 == 0:
                x2 = 25
            else:
                x2 = 37
            if i >= 0:                 
                painter.drawLine(x1, y1, x2, y2)
                print(x2, y2)            

def timerHandler(): 
    tape.setCurTime(tape.currTime+1)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = QGraphicsScene(QRectF(-10, -100, 200, 850))
    # scene.addItem(QGraphicsRectItem(scene.sceneRect()))
    
    tape = TimeElapsedTape()
    scene.addItem(tape)

    timer = QTimer()
    timer.setInterval(100)
    timer.timeout.connect(timerHandler)

    view = QGraphicsView()
    view.setScene(scene)
    view.show()
    timer.start()   
    sys.exit(app.exec_())           