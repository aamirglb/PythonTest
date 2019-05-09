import sys
from PySide2 import QtWidgets, QtGui, QtCore

def drawGrid(w, h, s):
	for i in range(0, w, 50):
		gridLines.insert(0, QtWidgets.QGraphicsLineItem(i, 0, i, sceneHeight))
		gridLines[0].setPen(QtGui.QPen(QtCore.Qt.lightGray))
		s.addItem(gridLines[0])

	for j in range(0, h, 50):
		gridLines.insert(0, QtWidgets.QGraphicsLineItem(0, j, w, j))
		gridLines[0].setPen(QtGui.QPen(QtCore.Qt.lightGray))
		s.addItem(gridLines[0])

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)

	# Create a graphics scene
	sceneWidth = 400
	sceneHeight = 400	

	scene = QtWidgets.QGraphicsScene(QtCore.QRectF(0, 0, sceneWidth, sceneHeight))
	rect = scene.sceneRect()

	gridLines = list()
	drawGrid(sceneWidth, sceneHeight, scene)

	line1 = QtWidgets.QGraphicsLineItem(sceneWidth/2, 0, sceneWidth/2, sceneHeight)
	line1.setPen(QtGui.QPen(QtCore.Qt.black, 2))
	scene.addItem(line1)

	line2 = QtWidgets.QGraphicsLineItem(0, sceneHeight/2, sceneWidth, sceneHeight/2)
	line2.setPen(QtGui.QPen(QtCore.Qt.red, 2))
	scene.addItem(line2)

	line3 = QtWidgets.QGraphicsLineItem(-50, -50, sceneWidth, sceneHeight)
	line3.setPen(QtGui.QPen(QtCore.Qt.blue, 2))
	line3.setFlag(QtWidgets.QGraphicsItem.ItemClipsChildrenToShape, True);
	scene.addItem(line3)

	scene.addItem(QtWidgets.QGraphicsRectItem(rect))
	# Create a graphics view
	view = QtWidgets.QGraphicsView()
	view.setScene(scene)
	view.show()

	sys.exit(app.exec_())


