import bluetooth

class BTServer:
	def __init__(self):
		self.host = ""
		self.port = 1

	def open(self):
		self.server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
		print("Created Bluetooth Socket")

	# Currently this class is a simple echo server.
	# It simply repeats back any data it is sent.
	def run(self):
		try:
			self.server.bind((self.host, self.port))
			print("Bluetooth Binding successful")
		except:
			print("Bluetooth Binding unsuccessful")
		self.server.listen(1)
		client, address = self.server.accept()
		try:
			while True:
				data = client.recv(1024)
				print(data)
				client.send(data)
		except:
			client.close()
			self.server.close()

# Demonstrates how to use the BTServer class.
# Using it in this way means that if it loses a connection it
# will just reopen and wait for another connection.
server = BTServer()
while True:
	server.open()
	server.run()
