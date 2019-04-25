import sys
from PySide2.QtWidgets import (QApplication, QWidget, QSpinBox, )
from PySide2.QtGui import (QRegExpValidator)
from PySide2.QtCore import (QRegExp)

class HexSpinBox(QSpinBox):
	def __init__(self):
		super(HexSpinBox, self).__init__()
		self.validator = QRegExpValidator(QRegExp("[0-9A-Fa-f]{1, 8}"), self)
		self.setRange(0, 255)

	# 3 possible return values, Invalid, Intermediate, Acceptable
	def validate(self, text, pos):
		return self.validator.validate(text, pos)

	def textFromValue(self, value):
		return hex(value)[2:].upper()

	def valueFromText(self, text):		
		try:
			ival = int(text, 16)
		except:
			ival = 0
		return ival
				

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = HexSpinBox()
	widget.show()
	sys.exit(app.exec_())

