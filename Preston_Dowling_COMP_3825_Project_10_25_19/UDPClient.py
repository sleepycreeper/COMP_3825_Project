kfrom socket import*
from UDPClientFunctions import*
import emoji

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = ''
userChoice = ''
topMenu = True

# First thing to do is tell the server the user's name
UDPClientFunctions.set_user(serverName, serverPort, clientSocket)

# I eventually want to add menu functionality 
# Top Menu paths: 1) Close client, 2) Log Out/ReLogin, 3) Chat Menu

while topMenu:

	# Send messages to the server
	UDPClientFunctions.talk_to_Server(serverName, serverPort, clientSocket);

	# Receive message from the server
	responseMessage, serverAddress = clientSocket.recvfrom(2048)

	print(responseMessage.decode())
	# print('Server Address: ', serverAddress)

clientSocket.close()




