import sys
import math

from PySide2 import QtWidgets, QtGui, QtCore

class FractionSlider(QtWidgets.QWidget):
	XMARGIN = 12.0
	YMARGIN = 5.0
	WSTRING = "999"

	valueChanged = QtCore.Signal(int, int)

	def __iniit__(self, numerator=0, denominator=10, parent=None):
		super(FractionSlider, self).__init__(parent)
		self.__numerator = numerator
		self.__denominator = denominator
		self.setFocusPolicy(QtCore.Qt.WheelFocus)
		self.setSizePolicy(QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.MinimumExpanding,
			QtWidgets.QSizePolicy.Fixed))

	def decimal(self):
		return self.__numerator / float(self.__denominator)

	def fraction(self):
		return self.__numerator, self.__denominator

	def setFraction(self, numerator, denominator=None):
		if denominator is not None:
			if 3 <= denominator <= 60:
				self.__denominator = denominator
			else:
				raise ValueError, "denominaor out of range"

		if 0 <= numerator <= self.__denominator:
			self.__numerator = numerator
		else:
			raise ValueError, "numerator out of range"

		self.update()
		self.updateGeometry()

	def mousePressEvent(self, event):
		if event.button() == QtCore.Qt.LeftButton:
			self.moveSlider(event.x())
			event.accept()
		else:
			QtWidgets.QWidget.mousePressEvent(self, event)

	def moveSlider(self, x):
		span = self.width() - (FractionSlider.XMARGIN * 2)
		offset = span - x + FractionSlider.XMARGIN

		numerator = int(round(self.__denominator * (1.0 - (offset / span))))
		numerator = max(0, min(numerator, self.__denominator))

		if numerator != self.__numerator:
			self.__numerator = numerator
			self.valueChanged.emit(self.__numerator, self.__denominator)
			self.update()

	def mouseMoveEvent(self, event):
		self.moveSlider(event.x())

	def keyPressEvent(self, event):
		change = 0
		if event.key() == Qt.Key_Home:
			change = -self.__denominator
		elif event.key() in (Qt.Key_Up, Qt.Key_Right):
			change = 1
		elif event.key() == Qt.Key_PageUp:
			change = (self.__denominator // 10) + 1
		elif event.key() in (Qt.Key_Down, Qt.Key_Left):
			change = -1
		elif event.key() == Qt.Key_PageDown:
			change = -((self.__denominator // 10) + 1)
		elif event.key() == Qt.Key_End:
			change = self.__denominator
		if change:
			numerator = self.__numerator
			numerator += change
			numerator = max(0, min(numerator, self.__denominator))
			if numerator != self.__numerator:
				self.__numerator = numerator
				self.valueChanged.emit(self.__numerator, self.__denominator)
				self.update()
			event.accept()
		else:
			QWidget.keyPressEvent(self, event)

	def sizeHint(self):
		return self.minimumSizeHint()			

	def minimumSizeHint(self):
		font = QtGui.QFont(self.font())
		font.setPointSize(font.pointSize() - 1)
		fm = QtGui.QFontMetricsF(font)
		return QtCore.QSize(fm.width(FractionSlider.WSTRING) * \
		self.__denominator, (fm.height() * 4) + FractionSlider.YMARGIN)

	def paintEvent(self, event=None):
		font = QtGui.QFont(self.font())
		font.setPointSize(font.pointSize() - 1)
		fm = QtGui.QFontMetricsF(font)
		fracWidth = fm.width(FractionSlider.WSTRING)
		indent = fm.boundingRect("9").width() / 2.0
		if not X11:
			fracWidth *= 1.5
		span = self.width() - (FractionSlider.XMARGIN * 2)
		value = self.__numerator / float(self.__denominator)

		painter = QtGui.QPainter(self)
		painter.setRenderHint(QtGui.QPainter.Antialiasing)
		painter.setRenderHint(QtGui.QPainter.TextAntialiasing)
		painter.setPen(self.palette().color(QWidgets.QPalette.Mid))
		painter.setBrush(self.palette().brush(QWidgets.QPalette.AlternateBase))
		painter.drawRect(self.rect())

		segColor = QtGui.QColor(Qt.green).dark(120)
		segLineColor = segColor.dark()
		painter.setPen(segLineColor)
		painter.setBrush(segColor)
		painter.drawRect(FractionSlider.XMARGIN,
			FractionSlider.YMARGIN, span, fm.height())
		textColor = self.palette().color(QWidgets.QPalette.Text)
		segWidth = span / self.__denominator
			segHeight = fm.height() * 2
		nRect = fm.boundingRect(FractionSlider.WSTRING)
		x = FractionSlider.XMARGIN
		yOffset = segHeight + fm.height()

		for i in range(self.__denominator + 1):
			painter.setPen(segLineColor)
			painter.drawLine(x, FractionSlider.YMARGIN, x, segHeight)
			painter.setPen(textColor)
			y = segHeight
			rect = QtCore.QRectF(nRect)
			rect.moveCenter(QtCore.QPointF(x, y + fm.height() / 2.0))
			painter.drawText(rect, Qt.AlignCenter, QString.number(i))
			y = yOffset
			rect.moveCenter(QtCore.QPointF(x, y + fm.height() / 2.0))
			painter.drawText(rect, Qt.AlignCenter,
			QString.number(self.__denominator))
			painter.drawLine(QtCore.QPointF(rect.left() + indent, y),
				QtCore.QPointF(rect.right() - indent, y))
			x += segWidth

		span = int(span)
		y = FractionSlider.YMARGIN - 0.5
		triangle = [QtCore.QPointF(value * span, y),
			QtCore.QPointF((value * span) + \
			(2 * FractionSlider.XMARGIN), y),
			QtCore.QPointF((value * span) + \
			FractionSlider.XMARGIN, fm.height())]

		painter.setPen(Qt.yellow)
		painter.setBrush(Qt.darkYellow)
		painter.drawPolygon(QPolygonF(triangle))

if __name__ == "__main__":

	app = QtWidgets.QApplication(sys.argv)
	dialog = FractionSlider()
	dialog.show()
	app.exec_()
