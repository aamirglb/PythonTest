import sys
from PySide2 import QtWidgets, QtGui, QtCore

class MailClient(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent)

		self.folderTreeWidget = QtWidgets.QTreeWidget()
		
		self.item1 = QtWidgets.QTreeWidgetItem(self.folderTreeWidget)
		self.item2 = QtWidgets.QTreeWidgetItem(self.folderTreeWidget)
		self.item1.setText(0, "Inbox")
		self.item2.setText(0, "Sent")

		self.folderTreeWidget.addTopLevelItems([self.item1, self.item2])		

		self.messageTreeWidget = QtWidgets.QTreeWidget()
		self.textEdit = QtWidgets.QTextEdit()

		self.rightSplitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
		self.rightSplitter.addWidget(self.messageTreeWidget)
		self.rightSplitter.addWidget(self.textEdit)
		self.rightSplitter.setStretchFactor(1, 1)

		self.mainSplitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
		self.mainSplitter.addWidget(self.folderTreeWidget)
		self.mainSplitter.addWidget(self.rightSplitter)
		self.mainSplitter.setStretchFactor(1, 1)
		self.setCentralWidget(self.mainSplitter)
		self.setWindowTitle(self.tr("Mail Client"))

class ZoomButtons(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.zoomInButton = QtWidgets.QToolButton(self)
		self.zoomInButton.setText('Zoom In')		
		self.zoomInButton.setIcon(QtGui.QIcon('zoom-in-2'))
		self.zoomInButton.adjustSize()
		self.zoomInButton.clicked.connect(self.zoomIn)

		self.zoomOutButton = QtWidgets.QToolButton(self)
		self.zoomOutButton.setText('Zoom Out')
		self.zoomOutButton.setIcon(QtGui.QIcon('zoom-out-2'))
		self.zoomOutButton.adjustSize()
		self.zoomOutButton.clicked.connect(self.zoomOut)

		self.mainLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addWidget(self.zoomInButton)
		self.mainLayout.addWidget(self.zoomOutButton)
		self.setLayout(self.mainLayout)

	def zoomIn(self):
		print('Zooming In...')

	def zoomOut(self):
		print('Zooming Out...')


class FindDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		QtWidgets.QDialog.__init__(self, parent)

		# *************************************************
		# Use Layout Manager for child widgets
		# *************************************************
		self.namedLabel = QtWidgets.QLabel('Name: ')
		self.namedLineEdit = QtWidgets.QLineEdit()
		self.lookInLabel = QtWidgets.QLabel('Look In: ')
		self.lookInLineEdit = QtWidgets.QLineEdit()
		self.subfoldersCheckBox = QtWidgets.QCheckBox('Include Subfolders')
		self.tableWidget = QtWidgets.QTableWidget()
		self.tableWidget.setColumnCount(4)
		self.tableWidget.setHorizontalHeaderLabels(['Name', 'In Folder', 'Size', 'Date' ])
		self.messageLabel = QtWidgets.QLabel('0 files found')
		self.findButton = QtWidgets.QPushButton('Find')
		self.stopButton = QtWidgets.QPushButton('Stop')
		self.closeButton = QtWidgets.QPushButton('Close')
		self.helpButton = QtWidgets.QPushButton('Help')

		self.leftLayout = QtWidgets.QGridLayout()
		self.leftLayout.addWidget(self.namedLabel, 0, 0)
		self.leftLayout.addWidget(self.namedLineEdit, 0, 1)
		self.leftLayout.addWidget(self.lookInLabel, 1, 0)
		self.leftLayout.addWidget(self.lookInLineEdit, 1, 1)
		self.leftLayout.addWidget(self.subfoldersCheckBox, 2, 0, 1, 2)
		self.leftLayout.addWidget(self.tableWidget, 3, 0, 1, 2)
		self.leftLayout.addWidget(self.messageLabel, 4, 0, 1, 2)

		self.rightLayout = QtWidgets.QVBoxLayout()
		self.rightLayout.addWidget(self.findButton)
		self.rightLayout.addWidget(self.stopButton)
		self.rightLayout.addWidget(self.closeButton)
		self.rightLayout.addStretch()
		self.rightLayout.addWidget(self.helpButton)

		self.mainLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.leftLayout)
		self.mainLayout.addLayout(self.rightLayout)
		self.setLayout(self.mainLayout)
		# self.mainLayout.setContentsMargins(20, 20, 20, 20 )
		# self.mainLayout.setSpacing(10)

		# *************************************************
		# Use Fixed and Manual Position for child widgets
		# *************************************************

		# self.namedLabel = QtWidgets.QLabel('Name: ', self)
		# self.namedLineEdit = QtWidgets.QLineEdit(self)
		# self.lookInLabel = QtWidgets.QLabel('Look In: ', self)
		# self.lookInLineEdit = QtWidgets.QLineEdit(self)
		# self.subfoldersCheckBox = QtWidgets.QCheckBox('Include Subfolders', self)
		# self.tableWidget = QtWidgets.QTableWidget(self)
		# self.tableWidget.setColumnCount(4)
		# self.tableWidget.setHorizontalHeaderLabels(['Name', 'In Folder', 'Size', 'Date' ])
		# self.messageLabel = QtWidgets.QLabel('0 files found', self)
		# self.findButton = QtWidgets.QPushButton('Find', self)
		# self.stopButton = QtWidgets.QPushButton('Stop', self)
		# self.closeButton = QtWidgets.QPushButton('Close', self)
		# self.helpButton = QtWidgets.QPushButton('Help', self)

		# self.namedLabel.setGeometry(9, 9, 50, 25)
		# self.namedLineEdit.setGeometry(65, 9, 200, 25)
		# self.lookInLabel.setGeometry(9, 40, 50, 25)
		# self.lookInLineEdit.setGeometry(65, 40, 200, 25)
		# self.subfoldersCheckBox.setGeometry(9, 71, 256, 23)
		# self.tableWidget.setGeometry(9, 100, 256, 100)
		# self.messageLabel.setGeometry(9, 206, 256, 25)
		# self.findButton.setGeometry(271, 9, 85, 32)
		# self.stopButton.setGeometry(271, 47, 85, 32)
		# self.closeButton.setGeometry(271, 84, 85, 32)
		# self.helpButton.setGeometry(271, 199, 85, 32)
		# self.setWindowTitle(self.tr("Find Files or Folders"))
		# # self.setFixedSize(365, 240)
		# self.setMinimumSize(265, 190)

	# def resizeEvent(self, event):
	# 	extraWidth = self.width() - self.minimumWidth()
	# 	extraHeight = self.height() - self.minimumHeight()
	# 	self.namedLabel.setGeometry(9, 9, 50, 25)
	# 	self.namedLineEdit.setGeometry(65, 9, 100 + extraWidth, 25)
	# 	self.lookInLabel.setGeometry(9, 40, 50, 25)
	# 	self.lookInLineEdit.setGeometry(65, 40, 100 + extraWidth, 25)
	# 	self.subfoldersCheckBox.setGeometry(9, 71, 156 + extraWidth, 23)
	# 	self.tableWidget.setGeometry(9, 100, 156 + extraWidth,
	# 	50 + extraHeight)
	# 	self.messageLabel.setGeometry(9, 156 + extraHeight, 156 + extraWidth,
	# 	25)
	# 	self.findButton.setGeometry(171 + extraWidth, 9, 85, 32)
	# 	self.stopButton.setGeometry(171 + extraWidth, 47, 85, 32)
	# 	self.closeButton.setGeometry(171 + extraWidth, 84, 85, 32)
	# 	self.helpButton.setGeometry(171 + extraWidth, 149 + extraHeight, 85,
	# 	32)

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	#*****************
	# Test Program 1
	#*****************
	# findDialog = FindDialog()
	# findDialog.show()

	#*****************
	# Test Program 2
	#*****************
	# editor1 = QtWidgets.QTextEdit()
	# editor2 = QtWidgets.QTextEdit()
	# editor3 = QtWidgets.QTextEdit()

	# splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
	# splitter.addWidget(editor1)
	# splitter.addWidget(editor2)
	# splitter.addWidget(editor3)

	# splitter.show()

	#*****************
	# Test Program 3
	#*****************
	# mail = MailClient()
	# mail.show()

	#*****************
	# Test Program 4
	#*****************
	zoom = ZoomButtons()
	zoom.show()
	sys.exit(app.exec_())