import sys
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton, QLineEdit, QDialog, QGroupBox,
	QHBoxLayout, QVBoxLayout, QGridLayout, QLayout)

class Window(QDialog):
	def __init__(self):
		super(Window, self).__init__()
		self.label = QLabel('Enter Your Age')
		self.lineEdit = QLineEdit()
		self.okButton = QPushButton('OK')
		self.moreButton = QPushButton('More')
		self.moreButton.setCheckable(True)		

		self.groupBox = QGroupBox()
		self.groupBox.setTitle('Details')
		self.nameLabel = QLabel('Name')
		self.nameLineEdit = QLineEdit()

		self.topLayout = QHBoxLayout()
		self.topLayout.addWidget(self.label)
		self.topLayout.addWidget(self.lineEdit)
		
		self.leftLayout = QVBoxLayout()
		self.leftLayout.addLayout(self.topLayout)
		self.leftLayout.addStretch()

		self.rightLayout = QVBoxLayout()
		self.rightLayout.addWidget(self.okButton)
		self.rightLayout.addWidget(self.moreButton)

		self.bottomLayout = QHBoxLayout()
		self.bottomLayout.addWidget(self.nameLabel)
		self.bottomLayout.addWidget(self.nameLineEdit)
		self.groupBox.setLayout(self.bottomLayout)
		self.groupBox.setVisible(False)
		self.moreButton.toggled.connect(lambda v: self.groupBox.setVisible(v))

		self.mainLayout = QGridLayout()
		self.mainLayout.addLayout(self.leftLayout, 0, 0)
		self.mainLayout.addLayout(self.rightLayout, 0, 1)
		# self.mainLayout.addLayout(self.bottomLayout, 1, 0)
		self.mainLayout.addWidget(self.groupBox)
		self.mainLayout.setSizeConstraint(QLayout.SetFixedSize);

		self.setLayout(self.mainLayout)

if __name__ == "__main__":
	app = QApplication(sys.argv)	
	mainWindow = Window();
	mainWindow.show();
	sys.exit(app.exec_())






