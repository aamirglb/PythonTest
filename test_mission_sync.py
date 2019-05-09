import sys
from PySide2 import QtWidgets, QtGui, QtCore, QtNetwork

class UserInterface(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)

		self.serverTester = None
		self.localIpLineEdit = QtWidgets.QLineEdit("127.0.0.1")
		self.localUdpPort = QtWidgets.QLineEdit("27027")
		self.remoteIp = QtWidgets.QLineEdit("127.0.0.1")
		self.remotePort = QtWidgets.QLineEdit("27000")

		# self.udpPortValidator = QtGui.QIntValidator(2001, 65535, self)
		# self.localUdpPort.setValidator(self.udpPortValidator)
		self.bindButton = QtWidgets.QPushButton('Bind Port')
		self.bindButton.clicked.connect(self.bindPort)

		self.infoBrowser = QtWidgets.QTextBrowser()

		self.startTestButton = QtWidgets.QPushButton('Start Test')
		self.startTestButton.setEnabled(False)
		self.startTestButton.clicked.connect(self.startTest)

		self.leftTop = QtWidgets.QGridLayout()
		self.leftTop.addWidget(QtWidgets.QLabel('Local IP: '), 0, 0)
		self.leftTop.addWidget(self.localIpLineEdit, 0, 1)
		self.leftTop.addWidget(QtWidgets.QLabel('UDP Port: '), 1, 0)
		self.leftTop.addWidget(self.localUdpPort, 1, 1)
		self.leftTop.addWidget(QtWidgets.QLabel('Remote IP: '), 2, 0)
		self.leftTop.addWidget(self.remoteIp, 2, 1)
		self.leftTop.addWidget(QtWidgets.QLabel('Remote Port: '), 3, 0)
		self.leftTop.addWidget(self.remotePort, 3, 1)

		self.leftTop.addWidget(self.bindButton, 4, 1, 1, 1)

		self.leftBottom = QtWidgets.QVBoxLayout()
		self.leftBottom.addWidget(self.startTestButton)

		self.leftLayout = QtWidgets.QVBoxLayout()
		self.leftLayout.addLayout(self.leftTop)
		self.leftLayout.addLayout(self.leftBottom)
		self.leftLayout.addStretch() 		

		self.mainLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.leftLayout)
		self.mainLayout.addWidget(self.infoBrowser)

		self.setLayout(self.mainLayout)
		self.setWindowTitle('PBY Mission Sync Test App')

	def bindPort(self):
		self.bindButton.setEnabled(False)
		self.startTestButton.setEnabled(True)
		if self.serverTester == None:
			self.serverTester = TestServer(self.localIpLineEdit.text(), 
				int(self.localUdpPort.text()), 
				self.remoteIp.text(), int(self.remotePort.text()), self)

	def startTest(self):
		# Send a packet to server
		self.serverTester.sendDatagramToRemoteHost(bytearray('0,0'.encode())) 

class TestServer(QtCore.QObject):
	ListingPort = 27027
	def __init__(self, ip, port, rip, rport, ui, parent=None):
		QtCore.QObject.__init__(self, parent)
		self.socket = QtNetwork.QUdpSocket(self)
		self.remoteIp = rip
		self.remotePort = rport
		
		if self.socket.bind(QtNetwork.QHostAddress(ip), port):
			ui.infoBrowser.append(f"Socket bond to UDP port {port}")			
		else:
			ui.infoBrowser.append(f"Failed to bind UDP port {port}")			

		self.socket.readyRead.connect(self.readPendingDatagrams)
		self.dgramCount = 0

	def readPendingDatagrams(self):
		while self.socket.hasPendingDatagrams():
			self.dgramCount += 1
			datagram = QtCore.QByteArray()
			datagram.resize(self.socket.pendingDatagramSize())
			(datagram, sender, senderPort) = self.socket.readDatagram(datagram.size())
			ui.infoBrowser.append(f'{self.dgramCount} => Received {datagram.size()} bytes from {sender}')

	def sendDatagramToRemoteHost(self, dg):
		self.socket.writeDatagram(dg, QtNetwork.QHostAddress(self.remoteIp), self.remotePort)


if __name__ == "__main__":
	# app = QtCore.QCoreApplication(sys.argv)
	app = QtWidgets.QApplication(sys.argv)
	window = UserInterface()
	window.show()
	sys.exit(app.exec_())



