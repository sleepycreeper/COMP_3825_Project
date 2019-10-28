import emoji
import datetime

class UDPServerFunctions:

	def detect_emojis(message):
		# This function will detect where the client wishes to use emojis in the message and convert them
		pass

	# Detects whether or not a user has chosen something for the server to do other than just chatting
	def detect_User_Chosen_Function():

		pass


	# Saves the chat log to a text file with the date and users who logged on while the server was active
	def save_Chat_Log(chatLog, users):
		print('\nSAVING CHAT LOG TO FILE')

		temp = '\nDate: '

		d = datetime.datetime.today()
		day, month, year = d.day, d.month, d.year

		temp += str(month) + '-' + str(day) +'-' + str(year)

		temp += '\nUsers Involved: '
		for i in range(len(users) - 1):
			if i == len(users) - 1:
				temp += users[i][0] + '\n'
			else:
				temp += users[i][0] + ', '

		file = open("ChatLogs.txt", "w")
		file.write(temp + chatLog)
		file.close()

		print('SAVE SUCCESSFUL\n')

	def get_User_Name(users, clientAddress):
		# The below code is for determinig which user's name gets attached to this line of the message being sent back to the client
		for u in users:
			if clientAddress == u[1]:
				return u[0]

	# Returns only the parts of a the chat log that the user hasn't seen yet
	def since_Last(chatLog, clientAddress, users, usersLastMessages):
		lastMessage = ''

		for u in users:
			if clientAddress == u[1]:
				lastMessage = usersLastMessages[u]

		if not(lastMessage == 'DEFAULT'):

			index = chatLog.index(lastMessage)
			#print('Check lastMessage: ', lastMessage)
			#print('Check index:', index)

			logSinceLast = chatLog[index:len(chatLog)-1]

			return logSinceLast
		else:
			return chatLog







