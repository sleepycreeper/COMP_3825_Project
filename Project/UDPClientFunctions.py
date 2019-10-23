class UDPClientFunctions():

	def send_Message_to_Server(serverName, serverPort, clientSocket):
		keep_looping = True
		temp_message = ''
		message = ''

		print('Here you can send a message to the server, you can only do one line at a time')
		print(' 	right now though. Type only \"send\" when you are ready to send to the server.')

		while keep_looping:
			temp_message = message
			message = input('Input: ')

			if message == 'send':
				message = temp_message
				keep_looping = False
				clientSocket.sendto(message.encode(), (serverName, serverPort))

			message = temp_message + message
