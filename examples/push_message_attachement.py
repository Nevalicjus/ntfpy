from ntfpy import NTFYServer, NTFYUser, NTFYClient, NTFYPushMessage, NTFYUrlAttachement

def main():
	server = NTFYServer('https://ntfy.sh')
	user = NTFYUser('user', 'pass')
	client = NTFYClient(server, 'test', user)
	message = NTFYPushMessage('And here you have an attachement')
	message.addTag('beginner')
	attachement = NTFYUrlAttachement('https://docs.ntfy.sh/static/img/ntfy.png')
	message.attachement = attachement
	client.send_message(message)

main()
