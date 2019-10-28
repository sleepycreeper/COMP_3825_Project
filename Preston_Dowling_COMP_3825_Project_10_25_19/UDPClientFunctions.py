class UDPClientFunctions():

	# The most basic method for sending a message to the server
	def send_Message(message, serverName, serverPort, clientSocket):
		clientSocket.sendto(message.encode(), (serverName, serverPort))



	# Talking to the server, not the most basic method
	def talk_to_Server(serverName, serverPort, clientSocket):
		keep_looping = True
		temp_message = ''
		message = ''

		#print('Here you can send a message to the server, you can only do one line at a time')
		#print(' 	right now though. Type only \"send\" when you are ready to send to the server.')

		while keep_looping:
			temp_message = message
			message = input('Input: ')

			if message == '/send':
				message = temp_message
				keep_looping = False
				clientSocket.sendto(message.encode(), (serverName, serverPort))

			if UDPClientFunctions.detect_Function_Request_From_User(message, serverName, serverPort, clientSocket) == True:
				keep_looping = False

			message = temp_message + message

	def detect_Function_Request_From_User(message, serverName, serverPort, clientSocket):

		if message == '/log':
			clientSocket.sendto('CHAT_LOG'.encode(), (serverName, serverPort))
			return True
		elif message == '/closeServer':
			clientSocket.sendto('CLOSE'.encode(), (serverName, serverPort))
			return True

		return False


	# Ask user to set their name so the server can know who is talking
	# This works by sending a message to the server with just the name and the server creates a USER object on its end
	def set_user(serverName, serverPort, clientSocket):

		message = input('Please tell the server your name: ')

		clientSocket.sendto('SET_USER'.encode(), (serverName, serverPort))
		clientSocket.sendto(message.encode(), (serverName, serverPort))

