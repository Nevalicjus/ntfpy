import time
from typing import Optional, Sequence

from .raw_send import raw_send
from .raw_subscribe import raw_subscribe

__all__ = [
    "NTFYClient",
    "NTFYMessage",
    "NTFYServer",
    "NTFYUser"
]

class NTFYServer():
    def __init__(self, url):
        self.url = url

class NTFYUser():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def auth(self) -> str :
        return f"{self.username}:{self.password}"

class NTFYClient():
    def __init__(self, server: NTFYServer, topic: str, user: Optional[NTFYUser] = None):
        self.server = server
        self.topic = topic
        self.user = user

    def send(self, message: str, title: Optional[str] = None, priority: Optional[str] = None, tags: Optional[str] = None, 
                   click: Optional[str] = None, attach: Optional[str] = None, actions: Optional[str] = None, 
                   email: Optional[str] = None, delay: Optional[str] = None):
        auth = self.user.auth() if self.user is not None else None
        raw_send(self.server.url, self.topic, message, auth = auth, title = title, priority = priority, tags = tags, click = click, attach = attach, actions = actions, email = email, delay = delay)

    async def subscribe(self):
        auth = self.user.auth() if self.user is not None else None
        await raw_subscribe(self.server.url, self.topic, auth = auth)

class NTFYMessage():
    def __init__(self, message: str, id: str, timestamp: int, topic: str, title: Optional[str] = None, 
                       priority: Optional[int] = None, tags: Optional[Sequence[str]] = None, click: Optional[str] = None, 
                       attach = None, actions = None, email: Optional[str] = None, delay = None):
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
