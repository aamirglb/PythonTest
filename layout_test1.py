import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QDialog, QComboBox, QGroupBox,
	QHBoxLayout, QVBoxLayout, QGridLayout, QLayout, QTableWidget, QTableWidgetItem, )
from PySide2.QtCore import (QFile, )
from PySide2.QtUiTools import QUiLoader

class Window(QDialog):
	def __init__(self):
		super(Window, self).__init__()
		self.label = QLabel('Enter Your Age')
		self.lineEdit = QLineEdit()
		self.label1 = QLabel('Year of Birth')
		self.combo1 = QComboBox()

		self.okButton = QPushButton('OK')
		self.moreButton = QPushButton('More')
		self.moreButton.setCheckable(True)		

		self.groupBox = QGroupBox()
		self.groupBox.setTitle('Details')
		self.nameLabel = QLabel('Name')
		self.nameLineEdit = QLineEdit()
		self.label3 = QLabel('Year of Birth')
		self.combo2 = QComboBox()

		self.topLayout1 = QHBoxLayout()
		self.topLayout1.addWidget(self.label)
		self.topLayout1.addWidget(self.lineEdit)

		self.topLayout2 = QHBoxLayout()	
		self.topLayout2.addWidget(self.label1)
		self.topLayout2.addWidget(self.combo1)
		for x in range(ord('A'), ord('F')):
			self.combo1.addItem(str(chr(x)))		
		
		self.leftLayout = QVBoxLayout()
		self.leftLayout.addLayout(self.topLayout1)
		self.leftLayout.addLayout(self.topLayout2)		
		self.leftLayout.addStretch()

		self.rightLayout = QVBoxLayout()
		self.rightLayout.addWidget(self.okButton)
		self.rightLayout.addWidget(self.moreButton)

		self.bottomLayout1 = QHBoxLayout()
		self.bottomLayout1.addWidget(self.nameLabel)
		self.bottomLayout1.addWidget(self.nameLineEdit)

		self.bottomLayout2 = QHBoxLayout()
		self.bottomLayout2.addWidget(self.label3)
		self.bottomLayout2.addWidget(self.combo2)		
		self.combo2.addItem("None")

		self.bottomLayout = QVBoxLayout()
		self.bottomLayout.addLayout(self.bottomLayout1)
		self.bottomLayout.addLayout(self.bottomLayout2)	

		self.groupBox.setLayout(self.bottomLayout)
		self.groupBox.setVisible(False)
		self.moreButton.toggled.connect(lambda v: self.groupBox.setVisible(v))

		self.combo2.setMinimumSize(self.combo2.sizeHint());

		self.mainLayout = QGridLayout()
		self.mainLayout.addLayout(self.leftLayout, 0, 0)
		self.mainLayout.addLayout(self.rightLayout, 0, 1)
		# self.mainLayout.addLayout(self.bottomLayout, 1, 0)
		self.mainLayout.addWidget(self.groupBox)
		self.mainLayout.setSizeConstraint(QLayout.SetFixedSize);

		self.setLayout(self.mainLayout)

	def title(self):
		return 'Window'

def cellName(r, c):
	r = r+1
	c = chr(ord('A') + c)
	print(f'Cell {c}{r} changed.')

if __name__ == "__main__":
	app = QApplication(sys.argv)
	if len(sys.argv) == 1:
		mainWindow = Window()
		mainWindow.show()
		for x in QApplication.topLevelWidgets():
			print(x.title())

	elif len(sys.argv) == 2:
		opt = int(sys.argv[1])
		if opt == 1:
			loader = QUiLoader()	
			file = QFile("dialog.ui")
			file.open(QFile.ReadOnly)
			myWidget = loader.load(file)
			file.close()
			myWidget.show()
		if opt == 2:
			table = QTableWidget(12, 10)
			for i in range(0, 10):
				item = QTableWidgetItem()
				item.setText(chr(ord('A')+i))
				table.setHorizontalHeaderItem(i, item)
			table.setShowGrid(Trued)					
			table.show()
			table.cellChanged.connect(cellName)
		else:
			app.aboutQt()
			sys.exit()
	sys.exit(app.exec_())






