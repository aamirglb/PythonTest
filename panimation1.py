import sys
from PySide2 import QtWidgets, QtGui, QtCore

class Ball(QtCore.QObject):
	def __init__(self, parent=None):
		super(Ball, self).__init__(parent)
		self.pixmap_item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap("ball.png"))

	def _set_pos(self, pos):
		self.pixmap_item.setPos(pos)

	pos = QtCore.Property(QtCore.QPointF, fset=_set_pos)


class Example(QtWidgets.QGraphicsView):
	def __init__(self, parent=None):
		super(Example, self).__init__(parent)
		self.initView()

	def initView(self):
		self.ball = Ball()

		self.anim = QtCore.QPropertyAnimation(self.ball, b'pos')
		self.anim.setDuration(10000)
		self.anim.setLoopCount(2)
		self.anim.setStartValue(QtCore.QPointF(5, 30))

		self.anim.setKeyValueAt(0.3, QtCore.QPointF(80, 30))
		self.anim.setKeyValueAt(0.5, QtCore.QPointF(200, 30))
		self.anim.setKeyValueAt(0.8, QtCore.QPointF(250, 250))

		self.anim.setEndValue(QtCore.QPointF(290, 30))

		self.scene = QtWidgets.QGraphicsScene(self)
		self.scene.setSceneRect(0, 0, 300, 300)
		self.scene.addItem(self.ball.pixmap_item)
		self.setScene(self.scene)

		self.setWindowTitle("Ball Animation")
		self.setRenderHint(QtGui.QPainter.Antialiasing)
		self.setGeometry(300, 300, 500, 350)

		self.anim.start()
		self.show()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())		