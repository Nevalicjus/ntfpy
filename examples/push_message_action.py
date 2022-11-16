from ntfpy import NTFYServer, NTFYUser, NTFYClient, NTFYPushMessage, NTFYViewAction

def main():
	server = NTFYServer('https://ntfy.sh')
	user = NTFYUser('user', 'pass')
	client = NTFYClient(server, 'test', user)
	message = NTFYPushMessage('With a cool button you can press', title = 'This is also a test')
	message.addTag('beginner')
	action = NTFYViewAction('I wonder what it does', 'https://youtu.be/dQw4w9WgXcQ')
	message.addAction(action)
	client.send_message(message)

main()
