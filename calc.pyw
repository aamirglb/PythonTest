import sys
import math
# import division
from PySide2 import QtWidgets, QtGui, QtCore

class Form(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)
		self.browser = QtWidgets.QTextBrowser()
		self.lineedit = QtWidgets.QLineEdit("Type an expression and press Enter")
		self.lineedit.selectAll()

		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(self.browser)
		layout.addWidget(self.lineedit)
		self.setLayout(layout)

		self.lineedit.setFocus()
		self.lineedit.returnPressed.connect(self.updateUi)		
		self.setWindowTitle("Expression Calculator")

	def updateUi(self):
		try:
			text = self.lineedit.text()
			self.browser.append(f"{text} = <b>{eval(text)}</b>")
		except:
			self.browser.append(f"<font color=red> {text} is invalid!</font>")
		self.lineedit.setText('')

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	form = Form()
	form.show()
	app.exec_()			



