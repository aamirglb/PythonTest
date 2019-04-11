import sys
#from PyQt5.QtWidgets import QApplication, QLabel, QHBoxLayout, QPushButton
#from PyQt5.QtWidgets import *

from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QMessageBox
from PySide2.QtCore import QByteArray
from PySide2.QtNetwork import QUdpSocket, QHostAddress, QNetworkDatagram

class Example(QWidget) :

	def get_field(self, data, offset, size) :
	    index = 0
	    field = ''
	    while( index < size ) :
	        field += data[offset + index]
	        index += 1

	    return field

	def __init__(self):
		super().__init__()
		self.layout = QVBoxLayout()
		self.initUI()
		self.udpSocket = QUdpSocket()
		self.udpSocket.bind(QHostAddress('127.0.0.1'), 7111)
		self.udpSocket.readyRead.connect(self.readPendingDatagrams)
				

	def initUI(self):
		''' Initialize the User Interface '''
		self.setGeometry(300, 300, 300, 220)
		self.setWindowTitle('Test App')		
		self.addButtons()
		self.setLayout(self.layout)
		self.show()

	def addButtons(self):
		self.layout.addWidget(QLabel('<H1><font color="red">Hello PyQt5</font></H1>'))
		buttonList = []
		numbers = ('one', 'two', 'three', 'four')
		for i in range(4):
			button = QPushButton(numbers[i])
			self.layout.addWidget(button)
			buttonList.insert(i, button)
			buttonList[i].clicked.connect(self.buttonClick)
			#self.layout.addWidget(QPushButton('Button ' + str(i)))
		self.line = QLineEdit()
		self.layout.addWidget(self.line)
		self.label = QLabel()
		self.layout.addWidget(self.label)
		self.line.textChanged.connect(self.label.setText)

	def buttonClick(self):
		button = self.sender()
		if isinstance(button, QPushButton):
			text = f'Button {button.text()}'
			print('button click event from ' + button.text())
			self.line.setText('')
			#datagram = QNetworkDatagram(bytes(text, 'utf-8'), QHostAddress.LocalHost, 45454)
			#self.udpSocket.writeDatagram(datagram)
			datagram = QByteArray(bytes(text, 'utf-8'))
			self.udpSocket.writeDatagram(datagram, QHostAddress('127.0.0.1'), 6010)

	def readPendingDatagrams(self):
		while self.udpSocket.hasPendingDatagrams():
			# datagram = QByteArray()
			# datagram.resize(self.udpSocket.pendingDatagramSize())

			(datagram, sender, senderPort) = self.udpSocket.readDatagram(1024)
			print(f'{sender.toString()}:{senderPort}')			
			self.processDatagram(datagram)

	def processDatagram(self, datagram):		
		pkt = list(datagram)
		# print(pkt)
		for i in range(0, len(pkt)):
			hex_val = hex(int.from_bytes(pkt[i], byteorder='big'))[2:]
			hex_val = hex_val.rjust(2, '0')
			# pkt[i] = str(hex_val)
			pkt[i] = chr(int(hex_val, 16))
		print(pkt)
		# msg_id = int(self.get_field(pkt, 14, 4), 16)
		# print(f'Message: {msg_id}')

	def closeEvent(self, event):
		pass
		# reply = QMessageBox.question(self, 'Message',
		# 	'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No,
		# 	QMessageBox.No)

		# if reply == QMessageBox.Yes:
		# 	event.accept()
		# else:
		# 	event.ignore()

	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
