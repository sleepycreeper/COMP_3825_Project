from socket import *
from UDPServerFunctions import*
import emoji

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', 12000))

print("The server is ready to receive: ")


users = []                                   # "users" is a list that will be filled with tuples of the form (userName, clientAddress)
usersLastMessages = {}                       # "usersLastMessages" key values will be individual users, data will be the last message send by that user

chatLog = ''
chatLogCounter = -1

while True:
	message, clientAddress = serverSocket.recvfrom(2048)
	#print('Message Check 1: ' + message.decode())

	# Check for requests from the client for specific functions, if not, assume just chatting
	if message.decode() == 'SET_USER':					# The client requests a new user to be set														       
		userName, clientAddress = serverSocket.recvfrom(2048)
		#print('Message Check 2: ' + userName.decode())

		lastMessageSent = 'DEFAULT'

		# Create a new user specified by the tuple (userName, clientAddress)
		newUser = (userName.decode(), clientAddress)
		users.append(newUser)

		usersLastMessages[newUser] = lastMessageSent

		#print('usersLastMessages Initialization Check:', usersLastMessages[newUser])

	elif message.decode() == 'CHAT_LOG':		# The user requests the entire chat log																			
		#print('Message Check 3: ' + message.decode())
		print(UDPServerFunctions.get_User_Name(users, clientAddress) + ' has requested the chat log.')

		serverSocket.sendto(chatLog.encode(), clientAddress)

	elif message.decode() == 'CLOSE':
		UDPServerFunctions.save_Chat_Log(chatLog, users)
		print('SHUTTING DOWN SERVER')
		serverSocket.close()
		exit()

	else:
		userName = UDPServerFunctions.get_User_Name(users, clientAddress)
		#print('USER NAME CHECK:', userName)


		newMessage = 'FROM ' + userName + ': ' + message.decode() + '\n'
		chatLogCounter += 1


		chatLog += newMessage

		responseMessage = '\n' + UDPServerFunctions.since_Last(chatLog, clientAddress, users, usersLastMessages) + '\n'

		# Set the lastMessageSent for this user to newMessage
		for u in users:
			if clientAddress == u[1]:
				#print(u[0] + '\'s lastMessageSent Before Update Check:', usersLastMessages[u])
				usersLastMessages[u] = newMessage
				#print(u[0] + '\'s lastMessageSent Update Check:', usersLastMessages[u])

		print('\nCURRENT CHAT LOG:\n' + chatLog + '\n')

		serverSocket.sendto(responseMessage.encode(), clientAddress)
		




	

