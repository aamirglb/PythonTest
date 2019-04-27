import sys
from PySide2.QtWidgets import (QApplication, QWidget, QSizePolicy,  )
from PySide2.QtCore import (Qt, QRect, QSize, )
from PySide2.QtGui import (QColor, QImage, qRgba, QPainter, )

class IconEditor(QWidget):
	def __init__(self):
		super(IconEditor, self).__init__()
		self.setAttribute(Qt.WA_StaticContents)
		self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
		self.curColor = Qt.black
		self.zoom = 8 * 4
		self.image = QImage(16, 16, QImage.Format_ARGB32)
		self.image.fill(qRgba(0, 0, 0, 0))

	def penColor(self):
		return self.curColor

	def setPenColor(self, newColor):
		self.curColor = newColor

	def zoomFactor(self):
		return self.zoom

	def setZoomFactor(self, newZoom):
		if newZoom < 1:
			newZoom = 1

		if newZoom != self.zoom:
			self.zoom = newZoom
			self.update()
			self.updateGeometry()			

	def iconImage(self):
		return self.image

	def setIconImage(self, newImage):
		if newImage != self.image:
			self.image = newImage.convertToFormat(QImage.Format_ARGB32)
			self.update()
			self.updateGeometry()		

	def sizeHint(self):
		size = self.zoom * self.image.size()
		if self.zoom >= 3:
			size += QSize(1, 1)
		return size
	
	def pixelRect(self, i, j):
		if self.zoom >= 3:
			return QRect(self.zoom * i + 1, self.zoom * j + 1,
				self.zoom -1, self.zoom -1)
		else:
			return QRect(self.zoom * i, self.zoom * j, self.zoom, self.zoom)

	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.setImagePixel(event.pos(), True)
			print('mouse left press')
		else:
			self.setImagePixel(event.pos(), False)
			print('mouse right press')

	def mouseMoveEvent(self, event):
		if event.buttons() & Qt.LeftButton:			
			self.setImagePixel(event.pos(), True)
		elif event.buttons() & Qt.RightButton:			
			self.setImagePixel(event.pos(), False)

	def setImagePixel(self, pos, opaque):
		i = pos.x() / self.zoom
		j = pos.y() / self.zoom
		if self.image.rect().contains(i, j):
			print(f'image contains {i}, {j}, {opaque}')
			if opaque:
				self.image.setPixel(i, j, Qt.black)
				print('setting pixel to black')
			else:
				self.image.setPixel(i, j, qRgba(0, 0, 0, 0))
		self.update(self.pixelRect(i,j))


	def paintEvent(self, event):
		painter = QPainter(self)
		if self.zoom >= 3:
			painter.setPen(self.palette().foreground().color())
			for i in range(0, self.image.width()):
				painter.drawLine(self.zoom * i, 0,
					self.zoom * i, self.zoom * self.image.height())	
			for j in range(0, self.image.height()):
				painter.drawLine(0, self.zoom * j, 
					self.zoom * self.image.width(), self.zoom * j)

		for i in range(0, self.image.width()):
			for j in range(0, self.image.height()):
				rect = self.pixelRect(i, j)
				
				if not event.region().intersects(rect):

					color = QColor.fromRgba(self.image.pixel(i, j))
					if color.alpha() < 255:
						painter.fillRect(rect, Qt.white)
					painter.fillRect(rect, color)					

	penColorProperty = property(QColor, penColor, setPenColor)
	iconImageProperty = property(QImage, iconImage, setIconImage)
	zoomFactorProperty = property(int, zoomFactor, setZoomFactor)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = IconEditor()
	window.show()
	sys.exit(app.exec_())
