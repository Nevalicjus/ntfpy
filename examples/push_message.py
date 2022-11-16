from ntfpy import NTFYServer, NTFYUser, NTFYClient, NTFYPushMessage

def main():
	server = NTFYServer('https://ntfy.sh')
	user = NTFYUser('user', 'pass')
	client = NTFYClient(server, 'test', user)
	message = NTFYPushMessage('Works great')
	message.title = 'This is a test'
	message.addTag('beginner')
	client.send_message(message)

main()
