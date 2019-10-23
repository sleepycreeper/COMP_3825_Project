from socket import*
from UDPClientFunctions import*



serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = ''

UDPClientFunctions.send_Message_to_Server(serverName, serverPort, clientSocket);

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())

clientSocket.close()




