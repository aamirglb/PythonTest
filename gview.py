from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, 
                               QLineEdit, QMessageBox, QMenu, QDialog, QHBoxLayout, QMenu, QAction,
                               QSlider,
                               QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsRectItem, 
                               QGraphicsTextItem, QGraphicsItem)
from PySide2.QtCore import (Qt, QFile, QSettings, QPoint, QSize, QByteArray, QRectF, QTimer)
from PySide2.QtGui import (QBrush, QPainter, QPen)

import sys

class MyView(QGraphicsView):
    def __init__(self):
        super(MyView, self).__init__()

class MyScene(QGraphicsScene):
    def __init__(self):
        super(MyScene, self).__init__()
        self.addEllipse(QRectF(0, 0, 50, 20))
        self.addRect(self.boundingRect())
        self.addRect(QRectF(150, 150, 100, 100))

    def boundingRect(self):
        return QRectF(0, 0, 200, 200)

class MyItem(QGraphicsItem):    
    def __init__(self, _id):
        super(MyItem, self).__init__()
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.itemId = _id
        self.scaleFactor = 1

    def paint(self, painter, options, widget):
        painter.scale(self.scaleFactor, self.scaleFactor)
        rect = self.boundingRect()
        if self.itemId == 1: 
            pen = QPen(Qt.red, 2)
            painter.drawRect(rect)
        else:
            pen = QPen(Qt.blue, 2)
            painter.drawEllipse(rect)

    def setScaleFactor(self, value):
        self.scaleFactor = value
        self.update()

    def boundingRect(self):
        return QRectF(0, 0, 100, 100)

    def contextMenuEvent(self, event):
        self.menu = QMenu()

        self.action = QAction(f'Item {self.itemId}')
        self.menu.addAction(self.action)        
        self.menu.exec_(event.screenPos())     


class MyDailog(QWidget):
    def __init__(self):
        super(MyDailog, self).__init__()
        self.setWindowTitle('Test')
        # self.scene = MyScene()
        # self.scene.setSceneRect(0, 0, 790, 525)

        
def sliderValueChanged(value):    
    item1.setScaleFactor(value/10)
    item2.setScaleFactor(value/10)        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyDailog()
    view = MyView()
    scene = MyScene()
    item1 = MyItem(1) 
    item2 = MyItem(2)   
    view.setScene(scene)
    view.fitInView(scene.boundingRect(), Qt.KeepAspectRatio)
    # scene.addItem(item1)
    # scene.addItem(item2)

    hSlider = QSlider()
    hSlider.setOrientation(Qt.Horizontal)
    hSlider.setRange(1, 10)
    hSlider.setValue(10)
    hSlider.valueChanged.connect(sliderValueChanged)
    layout = QHBoxLayout()
    layout.addWidget(view)
    # layout.addWidget(hSlider)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())