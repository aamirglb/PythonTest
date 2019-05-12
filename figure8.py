import math
import sys
from PySide2 import QtWidgets, QtGui, QtCore

class Widget(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(Widget, self).__init__(parent)
		self.setWindowTitle('Test Application')
		self.valueFigure8 = 250
		self.valueEllipse = 250

		self.changeFigure8 = False
		self.changeEllipse = False

	def sizeHint(self):
		return QtCore.QSize(600, 600)

	def paintEvent(self, event):
		
		items = []
		for i in range(64):    
		    items.append(i)

		painter = QtGui.QPainter(self)
		painter.setWindow(QtCore.QRect(-300, -300, 600, 600))
		# self.drawEllipse(painter)
		self.drawFigure8(painter)
		self.drawEllipse(painter)

	@QtCore.Slot(bool)
	def updateFigure8(self, status):
		self.changeFigure8 = status

	@QtCore.Slot(bool)
	def updateEllipse(self, status):
		self.changeEllipse = status

	@QtCore.Slot(int)
	def setValue(self, value):
		if self.changeFigure8:
			self.valueFigure8 = value

		if self.changeEllipse:
			self.valueEllipse = value

		if self.changeEllipse or self.changeFigure8:
			self.update()

	def drawEllipse(self, painter):
		ellipseState = []
		for i in range(64):		    
		    ellipseState.append(QtCore.QPointF(math.cos((i / 63.0) * 6.28) * self.valueEllipse,
		                    math.sin((i / 63.0) * 6.28) * self.valueEllipse))

		path = QtGui.QPainterPath()
		path.moveTo(ellipseState[0])

		for i in range(1, 64):
			path.lineTo(ellipseState[i])
			# print(f'{i}. {ellipseState[i]}')
			# painter.drawPoint(ellipseState[i])

		painter.setPen(QtGui.QPen(QtCore.Qt.red, 2))				
		painter.drawPath(path)


	def drawFigure8(self, painter):
		figure8State = []

		for i in range(64):
			# figure8State.append(QtCore.QPointF(math.sin((i / 63.0) * 6.28) * 250,
	  #                   math.sin(((i * 2)/63.0) * 6.28) * 250))
	  		figure8State.append(QtCore.QPointF(math.sin((i / 63.0) * 6.28) * self.valueFigure8,
	                    math.sin(((i * 2)/63.0) * 6.28) * self.valueFigure8))

		path = QtGui.QPainterPath()
		path.moveTo(figure8State[0])
		for i in range(1, 64):
			path.lineTo(figure8State[i])
		painter.setPen(QtGui.QPen(QtCore.Qt.blue, 2))
		painter.drawPath(path)	
			


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)

	pal = QtGui.QPalette()
	print(pal.color(QtGui.QPalette.Active, QtGui.QPalette.Window))

	window = Widget()
	slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
	slider.setRange(1, 400)
	slider.setValue(250)
	slider.valueChanged.connect(window.setValue)

	elipseCBox = QtWidgets.QCheckBox('Ellipse')
	elipseCBox.stateChanged.connect(window.updateEllipse)

	figure8CBox = QtWidgets.QCheckBox('Figure 8')
	figure8CBox.stateChanged.connect(window.updateFigure8)

	gview = QtWidgets.QGraphicsView()
	scene = QtWidgets.QGraphicsScene()
	scene.setBackgroundBrush(QtGui.QBrush(pal.color(QtGui.QPalette.Active, QtGui.QPalette.Window)))
	gview.setScene(scene)
	# gview.setBackgroundBrush(QtGui.QBrush(pal.color(QtGui.QPalette.Active, QtGui.QPalette.Window)))
	# gview.setBackgroundBrush(QtGui.QBrush(QtCore.Qt.black))

	layout = QtWidgets.QVBoxLayout()
	layout.addWidget(window)
	layout.addWidget(slider)
	layout.addWidget(elipseCBox)
	layout.addWidget(figure8CBox)
	layout.addWidget(gview)

	mainWindow = QtWidgets.QWidget()
	mainWindow.setLayout(layout)
	mainWindow.show()
	sys.exit(app.exec_())

    # # Figure 8.
    # figure8State.assignProperty(item, 'pos',
    #         QtCore.QPointF(math.sin((i / 63.0) * 6.28) * 250,
    #                 math.sin(((i * 2)/63.0) * 6.28) * 250))

    # # Random.
    # randomState.assignProperty(item, 'pos',
    #         QtCore.QPointF(-250 + QtCore.qrand() % 500,
    #                 -250 + QtCore.qrand() % 500))

    # # Tiled.
    # tiledState.assignProperty(item, 'pos',
    #         QtCore.QPointF(((i % 8) - 4) * kineticPix.width() + kineticPix.width() / 2,
    #                 ((i // 8) - 4) * kineticPix.height() + kineticPix.height() / 2))        