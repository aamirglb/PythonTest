import sys
from PySide2 import QtWidgets, QtGui, QtCore

class TeamLeadersDialog(QtWidgets.QDialog):
	def __init__(self, leaders, parent=None):
		super(TeamLeadersDialog, self).__init__(parent)
		self.model = QtCore.QStringListModel(self)
		self.model.setStringList(leaders)

		self.listView = QtWidgets.QListView()
		self.listView.setModel(self.model)
		self.listView.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed |
			QtWidgets.QAbstractItemView.DoubleClicked)

		self.buttonBox = QtWidgets.QDialogButtonBox()
		self.insertButton = self.buttonBox.addButton('&Insert', QtWidgets.QDialogButtonBox.ActionRole)
		self.deleteButton = self.buttonBox.addButton('&Delete', QtWidgets.QDialogButtonBox.ActionRole)
		self.buttonBox.addButton(QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.addButton(QtWidgets.QDialogButtonBox.Cancel)

		self.insertButton.clicked.connect(self.insert)
		self.deleteButton.clicked.connect(self.delete)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)
		
		self.mainLayout = QtWidgets.QVBoxLayout()
		self.mainLayout.addWidget(self.listView)
		self.mainLayout.addWidget(self.buttonBox)
		self.setLayout(self.mainLayout)

		self.setWindowTitle("Team Leaders")

	@QtCore.Slot(None)
	def insert(self):
		row = self.listView.currentIndex().row()
		self.model.insertRows(row, 1)

		index = self.model.index(row)
		self.listView.setCurrentIndex(index)
		self.listView.edit(index)

	@QtCore.Slot(None)
	def delete(self):
		self.model.removeRows(self.listView.currentIndex().row(), 1)

	def leaders(self):
		return self.model.stringList()


	def done(self, result):
		# if result == QtWidgets.QDialog.Accepted:
		# 	print('Accpeted')
		# else:
		# 	print('Rejected')

		for i, s in enumerate(self.leaders(), 1):
			print(f'{i}. {s}')
		qApp.quit()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	leaders = ["Stooge Viller" , "Littleface" , "B-B Eyes"
            , "Pruneface" ,   "Mrs. Pruneface" ,   "The Brow"
            , "Vitamin Flintheart" ,   "Flattop Sr." ,   "Shakey"
            , "Breathless Mahoney" ,   "Mumbles" ,   "Shoulders"]	

	dialog = TeamLeadersDialog(leaders)
	dialog.show()

	sys.exit(app.exec_())	