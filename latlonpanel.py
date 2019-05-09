import sys
from PySide2 import QtWidgets, QtGui, QtCore, QtPrintSupport

degree_sign= u'\N{DEGREE SIGN}'

def printGuide(entries):
	html = ''
	for s in entries:
		fields = entries.split(": ")
		title = fields[0].toHtmlEscaped()
		body = fields[1].toHtmlEscaped()
		print(title, body)

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)

	lat1 = QtWidgets.QLineEdit(f"N 000.000000{degree_sign}")
	lat2 = QtWidgets.QLineEdit(f"000{degree_sign} 00.000'")
	lat3 = QtWidgets.QLineEdit(f"000{degree_sign} 00' 00.0\"")
	lat1.setCursorPosition(2)
	lat1.setInputMask(f">A 099.000000 {degree_sign}")
	layout1 = QtWidgets.QHBoxLayout()
	layout1.addWidget(QtWidgets.QLabel('Latitude-1: '))
	layout1.addWidget(lat1)

	layout2 = QtWidgets.QHBoxLayout()
	layout2.addWidget(QtWidgets.QLabel('Latitude-2: '))
	layout2.addWidget(lat2)

	layout3 = QtWidgets.QHBoxLayout()
	layout3.addWidget(QtWidgets.QLabel('Latitude-3: '))
	layout3.addWidget(lat3)

	layout = QtWidgets.QVBoxLayout()
	layout.addLayout(layout1)
	layout.addLayout(layout2)
	layout.addLayout(layout3)

	widget = QtWidgets.QWidget()
	widget.setLayout(layout)
	widget.show()

	# printer = QtPrintSupport.QPrinter()
	# printDialog = QtPrintSupport.QPrintDialog(printer)
	# printDialog.exec()
	s = "Miltonopsis santanae: A most dangerous orchid species."
	printGuide(s)
	sys.exit(app.exec_())