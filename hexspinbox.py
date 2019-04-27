import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QSpinBox, QGridLayout)
from PySide2.QtGui import (QRegExpValidator)
from PySide2.QtCore import (QRegExp)

class HexSpinBox(QSpinBox):
	def __init__(self):
		super(HexSpinBox, self).__init__()
		self.validator = QRegExpValidator(QRegExp("[0-9A-Fa-f]{1, 8}"), self)
		self.setValidator(self.validator)		

	def setRangeMinMax(self, min, max):
		self.setRange(min, max)

	# 3 possible return values, Invalid, Intermediate, Acceptable
	def validate(self, text, pos):
		res = self.validator.validate(text, pos)
		print(res)
		return res

	def textFromValue(self, value):
		print(f'textFromValue: {value} => {hex(value)[2:].upper()}')
		return hex(value)[2:].upper()

	def valueFromText(self, text):
		print(f'valueFromText: {value}')	
		try:
			ival = int(text, 16)
		except:
			ival = 0
		return ival
				

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = QWidget()
	spinbox1 = HexSpinBox()
	spinbox2 = QSpinBox()
	spinbox1.setRangeMinMax(0, 100000)
	spinbox2.setRange(0, 100000)

	spinbox1.valueChanged.connect(spinbox2.setValue)
	spinbox2.valueChanged.connect(spinbox1.setValue)

	layout = QGridLayout()
	layout.addWidget(QLabel("Hex: "), 0, 0)
	layout.addWidget(spinbox1, 0, 1)
	# layout.addStretch()
	layout.addWidget(QLabel("Dec: "), 1, 0)
	layout.addWidget(spinbox2, 1, 1)
	window.setLayout(layout)
	window.show()
	sys.exit(app.exec_())

