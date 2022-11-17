from typing import Optional, Callable

from .server import NTFYServer
from .user import NTFYUser
from .message import NTFYMessage
from .push_message import NTFYPushMessage
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
            email: Optional[str] = None, delay: Optional[str] = None, icon: Optional[str] = None): 
        auth = self.user.auth() if self.user is not None else None
        raw_send(self.server.url, self.topic, message, auth = auth, title = title, priority = priority, tags = tags, click = click, attach = attach, actions = actions, email = email, delay = delay, icon = icon)
        
    def send_message(self, message: NTFYPushMessage):
        priority = str(message.priority) if message.priority is not None else None
        attachment = None
        if message.attachment is not None:
            attachment = message.attachment.url
        self.send(message.message, title = message.title, priority = priority, tags = message.tags, click = message.click_url, attach = attachment, actions = message.actions, email = message.email, delay = message.delay, icon = message.icon_url)

    async def subscribe(self, func: Callable[[NTFYMessage], None] = print):
        auth = self.user.auth() if self.user is not None else None
        await raw_subscribe(self.server.url, self.topic, auth = auth, func = func)
