import requests
import base64
import time
import json

__all__ = [
    "NTFYClient",
    "NTFYMessage",
    "NTFYServer",
    "NTFYUser"
]

class NTFYClient():
    def __init__(self, server, topic, user = None):
        self.server = server
        self.topic = topic
        self.user = user

    def send(self, message, title = None, priority = None, tags = None, click = None, attach = None, actions = None, email = None, delay = None):
        headers = {}
        if self.user != None:
            auth = f"{self.user.username}:{self.user.password}"
            auth_bytes = auth.encode("ascii")
            b64_bytes = base64.b64encode(auth_bytes)
            b64_s = b64_bytes.decode("ascii")
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
        r = requests.post(f"{self.server.url}/{self.topic}", headers = headers, data = message)

    async def subscribe(self):
        headers = {}
        if self.user != None:
            auth = f"{self.user.username}:{self.user.password}"
            auth_bytes = auth.encode("ascii")
            b64_bytes = base64.b64encode(auth_bytes)
            b64_s = b64_bytes.decode("ascii")
            headers["Authorization"] = f"Basic {b64_s}"
        r = requests.get(f"{self.server.url}/{self.topic}/json", stream = True, headers = headers)
        for l in r.iter_lines():
            if l:
                d = json.loads(l.decode("utf-8"))
                if d["event"] == "message":
                    m = NTFYMessage(d["message"], d["id"], d["time"], d["topic"])
                    for x in ["title", "priority", "tags", "click", "attach", "actions", "email", "delay"]:
                        if x in d:
                            setattr(m, x, d[x])
                    print(m)
                else:
                    print(d)

class NTFYMessage():
    def __init__(self, message, id, timestamp, topic, title = None, priority = None, tags = None, click = None, attach = None, actions = None, email = None, delay = None):
        self.message = message
        self.id = id
        self.timestamp = timestamp
        self.topic = topic
        self.title = title
        self.priority = priority
        self.tags = tags
        self.click = click
        self.attach = attach
        self.actions = actions
        self.email = email
        self.delay = delay
    
    def __str__(self):
        return f"{self.id} @ {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.timestamp))}\n{self.topic}: {self.message}"

class NTFYServer():
    def __init__(self, url):
        self.url = url

class NTFYUser():
    def __init__(self, username, password):
        self.username = username
        self.password = password