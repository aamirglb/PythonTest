import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, 
                               QLineEdit, QMessageBox, QMenu,
                               QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsTextItem, QGraphicsItem)
from PySide2.QtCore import (Qt, QFile, QSettings, QPoint, QSize, QByteArray, QRectF)
from PySide2.QtGui import (QBrush, QPainter, QPen)

class BracketItem(QGraphicsItem):
    def __init__(self, id):
        super(BracketItem, self).__init__()
        self.bracketId = id
        slotId = (id - 1) * 3
        self.rootSlot = SlotItem(slotId+1, 120, 20)
        self.leftChild = SlotItem(slotId+2, 20, 140)
        self.rightChild = SlotItem(slotId+3, 220, 140)
        self.rootSlot.setParentItem(self)
        self.leftChild.setParentItem(self)
        self.rightChild.setParentItem(self)

    def boundingRect(self):
        return QRectF(0, 0, 340, 230)

    def drawNodes(self):
        self.rootSlot.update()
        self.leftChild.update()
        self.rightChild.update()

    def paint(self, painter, option, widget):
        rect = self.boundingRect()
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawRect(rect)
        painter.drawLine(170, 90, 70, 140)
        painter.drawLine(170, 90, 270, 140)
                
        # painter.drawRect(self.rootSlot.boundingRect())
        # painter.drawRect(self.leftChild.boundingRect())
        # painter.drawRect(self.rightChild.boundingRect())

class SlotItem(QGraphicsItem):
    def __init__(self, id, posX, posY):
        super(SlotItem, self).__init__()
        self.pressed = False
        # self.setFlag(QGraphicsItem.ItemIsMovable)
        self.slotId = id
        self.text = str(id)
        self.startX = posX
        self.startY = posY
        self.width = 100
        self.height = 70

    def boundingRect(self):
        return QRectF(self.startX, self.startY, self.width, self.height)

    def paint(self, painter, option, widget):
        rect = self.boundingRect()

        # print(rect)
        # if self.pressed:
        #   pen = QPen(Qt.red, 3)
        #   painter.setPen(pen)
        #   painter.drawEllipse(rect)           
        # else:
        pen = QPen(Qt.black, 3)
        font = painter.font()
        font.setPixelSize(12)
        painter.setFont(font)
        painter.setPen(pen)
        painter.drawRect(rect)
        painter.drawText(self.startX+5, self.startY+20, f'Slot-{self.text}')
        # Draw a LED at right corner
        brush = QBrush()
        brush.setStyle(Qt.SolidPattern)
        if self.slotId % 3 == 0:
            brush.setColor(Qt.red)
        elif self.slotId % 2 == 0:
            brush.setColor(Qt.green)
        else:
            brush.setColor(Qt.cyan)

        # brush.setColor(Qt.red)
        painter.setBrush(brush)
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(Qt.blue)
        painter.setPen(pen)
        painter.drawEllipse(self.startX+5+80, self.startY+5, 10, 10)
    
    def mousePressEvent(self, event):
        self.pressed = True
        self.update()
        QGraphicsItem.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event):
        self.pressed = False
        self.update()
        QGraphicsItem.mouseReleaseEvent(self, event)

    def contextMenuEvent(self, event):
        print('Context menu Event')
        menu = QMenu()
        menu.addAction(f'Slot-{self.text} Action 1', lambda : print(f'Slot-{self.text} Action 1'))
        menu.addAction(f'Slot-{self.text} Action 2', lambda : print(f'Slot-{self.text} Action 2'))
        menu.exec_(event.screenPos())
        # menu.exec_(event.globalPos()")
        # action = menu.exec(event.screenPos())
        # menu.popup(event.screenPos())


class MainWindow(QMainWindow):
    def __init__(self):
        # super(MainWindow, self).__init__()
        super().__init__()

        # self.ui = QMainWindow()
        self.label = QLabel(f'<h1>Hello World</h1>')
        self.setGeometry(10, 70, 1000, 700)
        
        self.view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 800, 520)
        self.view.setScene(self.scene)

        # greenBrush = QBrush(Qt.green)
        # blueBrush = QBrush(Qt.blue)
        # outlinePen = QPen(Qt.black)
        # outlinePen.setWidth(2)

        # self.rectangle = self.scene.addRect(100, 0, 80, 100, outlinePen, blueBrush)
        # self.ellipse = self.scene.addEllipse(0, -100, 300, 60, outlinePen, greenBrush)
        # self.text = self.scene.addText('Hello World')

        # item = SlotItem(1);
        # self.scene.addItem(item)
        self.bracket1 = BracketItem(1)
        self.bracket1.setPos(10, 10)
        self.bracket2 = BracketItem(2)
        self.bracket2.setPos(10, 300)

        self.bracket3 = BracketItem(3)
        self.bracket3.setPos(450, 10)
        self.bracket4 = BracketItem(4)
        self.bracket4.setPos(450, 300)

        self.scene.addItem(self.bracket1)
        self.scene.addItem(self.bracket2)
        self.scene.addItem(self.bracket3)
        self.scene.addItem(self.bracket4)
        # self.bracket1.drawNodes()
        self.setCentralWidget(self.view)

    # def createMenus(self):
    #   self.fileMenu = menuBar()->addMenu(tr("&File"));
 #      fileMenu->addAction(newAct)
 #      fileMenu->addAction(openAct)
 #      fileMenu->addAction(saveAct)

print(sys.prefix)
print(sys.version)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    # button = QPushButton('Test')
    # window.setCentralWidget(button)
    # window.setGeometry(300, 300, 400, 400)
    # window.showMaximized()
    window.show()
    print('here')
    sys.exit(app.exec_())



