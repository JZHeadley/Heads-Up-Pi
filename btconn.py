import bluetooth

host = ""
port = 1

server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print("Created Bluetooth Socket")

try:
	server.bind((host, port))
	print("Bluetooth Binding Succeeded")
except:
	print("Bluetooth Binding Failed")

server.listen(1)

client, address = server.accept()
print("Connected to", address)
print("Client", client)
try:
    while True:
        data = client.recv(1024)
        print(data)
        client.send(data)
except:
    client.close()
    server.close()
