import sys
from PySide2 import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent)
		self.textEdit = QtWidgets.QTextEdit()
		self.setCentralWidget(self.textEdit)

		self.textEdit.setAcceptDrops(False)
		self.setAcceptDrops(True)

		self.setWindowTitle("Text Editor")

	def dragEnterEvent(self, event):
		if event.mimeData().hasFormat("text/uri-list"):
			event.acceptProposedAction()

	def dropEvent(self, event):
		urls = event.mimeData().urls()
		if len(urls) == 0:
			return
		print(urls[0])
		fileName = urls[0].toLocalFile()
		if fileName == '':
			return
		if self.readFile(fileName) :
			self.setWindowTitle(f"{fileName} - 'Drag File' ")

	def readFile(self, filename):
		file = QtCore.QFile(filename)
		print(filename)
		if file.open(QtCore.QIODevice.ReadOnly):
			print('File Opened for reading')
			stream = QtCore.QTextStream(file)
			self.textEdit.setPlainText(stream.readAll())
			return True
		else:
			print('Fail to open file')
			return False


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	widget = MainWindow()
	widget.show()
	sys.exit(app.exec_())