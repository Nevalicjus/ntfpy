from requests import Response
from typing import Optional, Callable, Final, Sequence

from .server import NTFYServer
from .user import NTFYUser
from .message import NTFYMessage
from .push_message import NTFYPushMessage, PRIORITY
from .actions import NTFYAction
from .attachments import NTFYUrlAttachment
from ..raw_send import raw_send, raw_send_message
from ..raw_subscribe import raw_subscribe

__all__ = [
    "NTFYClient"
]

class NTFYClient():
    def __init__(self, server: NTFYServer, topic: str, user: Optional[NTFYUser] = None):
        self.server: Final[NTFYServer]  = server
        self.topic:  Final[str]         = topic
        self.user:   Optional[NTFYUser] = user

    def send(self, message: str, title: Optional[str] = None, priority: Optional[PRIORITY] = None, tags: Optional[str] = None, 
            click: Optional[str] = None, attach: Optional[NTFYUrlAttachment] = None, actions: Optional[Sequence[NTFYAction]] = None, 
            email: Optional[str] = None, delay: Optional[str] = None, icon: Optional[str] = None) -> Response: 
        auth = self.user.auth() if self.user is not None else None
        return raw_send(self.server.url, self.topic, message, auth = auth, title = title, priority = priority, tags = tags, click = click, attach = attach, actions = actions, email = email, delay = delay, icon = icon)
        
    def send_message(self, message: NTFYPushMessage) -> Response:
        auth = self.user.auth() if self.user is not None else None
        return raw_send_message(self.server.url, self.topic, message, auth = auth)
        
    async def subscribe(self, func: Callable[[NTFYMessage], None] = print):
        auth = self.user.auth() if self.user is not None else None
        await raw_subscribe(self.server.url, self.topic, auth = auth, func = func)
