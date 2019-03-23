import bluetooth

class BTServer:
	def __init__(self):
		self.host = ""
		self.port = 1

	def open(self):
		self.server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
		print("Created Bluetooth Socket")

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

server = BTServer()
while True:
	server.open()
	server.run()
