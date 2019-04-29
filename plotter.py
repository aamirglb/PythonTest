import sys
from PySide2 import QtWidgets, QtGui, QtCore, Qt

class PlotSettings():
	def __init__(self):
		pass

class Plotter(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.setBackgroundRole(QtGui.QPalette.Dark)
		self.setAutoFillBackground(True)
		self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		self.setFocusPolicy(Qt.StrongFocus)
		self.rubberBandIsShown = False

		self.zoomInButton = QtWidgets.QToolButton(self)
		self.zoomInButton.setText('Zoom In')
		# self.zoomInButton.setIcon()
		self.zoomInButton.adjustSize()
		self.zoomInButton.clicked.connect(self.zoomIn)

		self.zoomOutButton = QtWidgets.QToolButton(self)
		self.zoomOutButton.setText('Zoom Out')
		self.zoomOutButton.adjustSize()
		self.zoomOutButton.clicked.connect(self.zoomOut)

		self.setPlotSettings(PlotSettings())
		self.zoomStack = list()
		self.curveMap = dict()
		self.pixmap = QtGui.QPixmap()
		self.rubberBandRect = QtGui.QRect()
		self.Margin = 50

	def setPlotSettings(self, settings):
		self.zoomStack.clear()
		self.zoomStack.append(settings)
		self.curZoom = 0
		self.zoomOutButton.hide()
		self.refreshPixmap()

	def zoomOut(self):
		if self.curZoom > 0:
			self.curZoom -= 1
			self.zoomOutButton.setEnabled(self.curZoom > 0)
			self.zoomInButton.setEnabled(True)
			self.zoomInButton.show()
			self.refreshPixmap()

	def zoomIn(self):
		if self.curZoom < (len(self.zoomStack) - 1):
			self.curZoom += 1
			self.zoomInButton.setEnabled(self.curZoom < (len(self.zoomStack) - 1))
			self.zoomOutButton.setEnabled(True)
			self.zoomOutButton.show()
			self.refreshPixmap()

	def setCurveData(self, id, data):
		self.curveMap[id] = data
		self.refreshPixmap()

	def clearCurve(self, id):
		self.curveMap.pop(id, None)
		self.refreshPixmap()

	def minimumSizeHint(self):
		return QtWidgets.QSize(6 * self.Margin, 4 * self.Margin)

	def sizeHint(self):
		return QtWidgets.QSize(12 * self.Margin, 8 * self.Margin)

	def paintEvent(self, event):
		painter = QtGui.QStylePainter(self)
		painter.drawPixmap(0, 0, self.pixmap)

		if self.rubberBandIsShown:
			painter.setPen(self.palette().light().color())
			painter.drawRect(self.rubberBandRect.normalized().adjusted(0, 0, -1, -1))

		if self.hasFocus():
			option = QtGui.QStyleOptionFocusRect()
			option.initFrom(self)
			option.backgroundColr = self.palette().dark().color()
			painter.drawPrimitive(QtGui.QStyle.PE_FrameFocusRect, option)

	def resizeEvent(self, event):
		x = self.width() - (self.zoomInButton.width() +
			self.zoomOutButton.width() + 10)
		self.zoomInButton.move(x, 5)
		self.zoomOutButton.move(x+self.zoomInButton.width() + 5, 5)
		self.refreshPixmap()

	def mousePressEvent(self, event):
		rect = QtGui.QRect(self.Margin, self.Margin,
			self.width() - 2 * self.Margin, self.heigh() - 2 * self.Margin)

		if event.button() == QtGui.Qt.LeftButton:
			if rect.contains(event.pos()):
				self.rubberBandIsShown = True
				self.rubberBandRect.setTopLeft(event.pos())
				self.rubberBandRect.setBottomRight(event.pos())
				self.updateRubberBandRegion()
				self.setCursor(QtGui.Qt.CrossCursor)

	def mouseMoveEvent(self, event):
		if self.rubberBandIsShown:
			self.updateRubberBandRegion()
			self.rubberBandRect.setBottomRight(event.pos())
			self.updateRubberBandRegion()

	def mouseReleaseEvent(self, event):
		if (event.button() == QtGui.Qt.LeftButton) and self.rubberBandIsShown:
			self.rubberBandIsShown = False
			self.updateRubberBandRegion();
			self.unsetCursor()

			rect = QtGui.QRect(self.rubberBandRect.normalized())
			if rect.width() < 4 or rect.height() < 4:
				return
			rect.translate(-self.Margin, -self.Margin)

			previousSettings = self.zoomStack[self.curZoom]
			settings = PlotSettings()
			dx = previousSettings.spanX() / (self.width() - 1 * self.Margin)
			dy = previousSettings.spanY() / (self.height() - 2 * self.Margin)
			settings.minX = previousSettings.minX + dx * rect.left()
			settings.maxX = previousSettings.minX + dx * rect.right()
			settings.minY = previousSettings.maxY - dy * rect.bottom()
			settings.maxY = previousSettings.maxY - dy * rect.top()
			settings.adjust()

			self.zoomStack.resize(self.curZoom + 1)
			self.zoomStack.append(settings)
			self.zoomIn()

	def keyPressEvent(self, event):
		if event.key() == QtGui.Qt.Key_Plus:
			self.zoomIn()
		elif event.key() == QtGui.Qt.Key_Minus:
			self.zoomOut()
		elif event.key() == QtGui.Qt.Key_Left:
			self.zoomStack[self.curZoom].scroll(-1, 0)
			self.refreshPixmap()
		elif event.key() == QtGui.Qt.Key_Right:
			self.zoomStack[self.curZoom].scroll(+1, 0)
			self.refreshPixmap()
		elif event.key() == QtGui.Qt.Key_Down:
			self.zoomStack[self.curZoom].scroll(0, -1)
			self.refreshPixmap()
		elif event.key() == QtGui.Qt.Key_Up:
			self.zoomStack[self.curZoom].scroll(0, +1)
			self.refreshPixmap()
		else:
			QtWidgets.QWidget.keyPressEvent(event)
