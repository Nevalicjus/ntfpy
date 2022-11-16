from ntfpy import NTFYServer, NTFYUser, NTFYClient, NTFYPushMessage, NTFYUrlAttachment

def main():
	server = NTFYServer('https://ntfy.sh')
	user = NTFYUser('user', 'pass')
	client = NTFYClient(server, 'test', user)
	message = NTFYPushMessage('And here you have an attachment')
	message.addTag('beginner')
	attachment = NTFYUrlAttachment('https://docs.ntfy.sh/static/img/ntfy.png')
	message.attachment = attachment
	client.send_message(message)

main()
