from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', 12000))

print("The server is ready to receive: ")

while True:
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = 'FROM SERVER: ' + message.decode()
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)

