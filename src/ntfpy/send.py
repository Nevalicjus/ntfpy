import requests
import base64

__all__ = (
    'send'
)

def send(server, topic, message, auth = None, title = None, priority = None, tags = None, click = None, attach = None, actions = None, email = None, delay = None):
    headers = {}
    if auth != None:
        auth_bytes = auth.encode('ascii')
        b64_bytes = base64.b64encode(auth_bytes)
        b64_s = b64_bytes.decode('ascii')
        headers["Authorization"] = f"Basic {b64_s}"
    if title != None:
        headers["Title"] = title
    if priority != None:
        headers["Priority"] = priority
    if tags != None:
        headers["Tags"] = tags
    if click != None:
        headers["Click"] = click
    if attach != None:
        headers["Attach"] = attach
    if actions != None:
        headers["Actions"] = actions
    if email != None:
        headers["Email"] = email
    if delay != None:
        headers["Delay"] = delay
    r = requests.post(f"{server}/{topic}", headers = headers, data = message)