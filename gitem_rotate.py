import sys
from PySide2 import QtWidgets, QtCore, QtGui

class GraphicsEllipseItem(QtWidgets.QGraphicsEllipseItem):
	def __init__(self, parent=None):
		QtWidgets.QGraphicsEllipseItem.__init__(self, parent)
		self.initialPos = QtCore.QPointF()
		self.rotation = 0
		self.setFlags(self.flags() | QtWidgets.QGraphicsItem.ItemIsSelectable)

	def mousePressEvent(self, event):
		self.initalPos = self.mapToScene(event.pos())		
		QtWidgets.QGraphicsItem.mousePressEvent(event)

	def mouseMoveEvent(self, event):		
		pos = QtCore.QPointF(self.mapToScene(event.pos()))

		if pos.y() > self.initalPos.y() :
			self.rotation += 1
		else:
			self.rotation -= 1

		if True:
			xform = QtGui.QTransform()
			xform.rotate(self.rotation)
			self.setTransform(xform)
		else:
			self.setRotation(self.rotation)

		self.initialPos = pos


class GraphicsView(QtWidgets.QGraphicsView):
	def __init__(self):
		QtWidgets.QGraphicsView.__init__(self)
		self.scene = QtWidgets.QGraphicsScene()
		self.setScene(self.scene)

		self.rect1 = QtCore.QRect(10, 10, 80, 60)
		self.rect2 = QtCore.QRect(50, 80, 80, 60)

		self.item1 = GraphicsEllipseItem()
		self.item1.setRect(-40, -30, 80, 60)
		self.scene.addItem(self.item1)

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	box = GraphicsView()
	box.show()
	sys.exit(app.exec_())
