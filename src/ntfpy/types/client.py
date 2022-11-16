from typing import Optional

from .server import NTFYServer
from .user import NTFYUser
from ..raw_send import raw_send
from ..raw_subscribe import raw_subscribe

__all__ = [
    "NTFYClient"
]

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
