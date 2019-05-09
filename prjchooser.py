import sys
from PySide2 import QtWidgets, QtGui, QtCore

class ProjectListWidget(QtWidgets.QListWidget):
	def __init__(self, parent=None):
		QtWidgets.QListWidget.__init__(self, parent)
		self.setAcceptDrops(True)
		self.startPos = QPoint(0, 0)

	def mousePressEvent(self, event):
		if event.button() == QtCore.Qt.LeftButton:
			self.startPos = QtCore.QPoint(event.pos())
		QtWidgets.QListWidget.mousePressEvent(event)

	def mouseMoveEvent(self, event):
		if event.button() & QtCore.Qt.LeftButton:
			distance = (event.pos() - self.startPos).manhattanLength()
			if distance >= QtWidgets.QApplication.startDragDistance():
				self.performDrag()
		QtWidgets.QListWidget.mouseMoveEvent(event)

	def performDrag(self):
		item = self.currentItem()
		if item:
			mimeData = QtCore.QMimeData()
			mimeData.setText(item.text())

			drag = QtGui.QDrag(self)
			drag.setMimeData(mimeData)
			drag.setPixmap(QPixmap('person.png'))
			if drag.exec(QtCore.Qt.MoveAction) == QtCore.Qt.MoveAction:
				pass

	def dragEnterEvent(self, event):
		source = event.source()
		if source and (not isinstance(source, self)):
			event.setDropAction(QtCore.Qt.MoveAction)
			event.accept()
		else:
			print('dragEnter condition failed')

	def dragMoveEvent(self, event):
		source = event.source()
		if source and (not isinstance(source, self)):
			event.setDropAction(QtCore.Qt.MoveAction)
			event.accept()

	def dropEvent(self, event):
		source = event.source()

		if source and (not isinstance(source, self)):
			self.addItem(event.mimeData().text())
			event.setDropAction(QtCore.Qt.MoveAction)
			event.accept()