from requests import Response
from typing import Optional, Callable, Final, Sequence

from .server import NTFYServer
from .actions import NTFYAction
from .attachments import NTFYUrlAttachment
from .message import NTFYMessage
from .push_message import NTFYPushMessage, PRIORITY
from .user import NTFYUser
from ..raw_send import raw_send, raw_send_message
from ..raw_subscribe import raw_subscribe

__all__ = [
    "NTFYClient"
]

class NTFYClient():
    """
    Attributes
    ----------
    server: :class:`NTFYServer`
    topic: :class:`str`
    user: Optional[:class:`NTFYUser`]
    """
    def __init__(self, server: NTFYServer, topic: str, user: Optional[NTFYUser] = None):
        self.server: Final[NTFYServer] = server
        self.topic: Final[str] = topic
        self.user: Optional[NTFYUser] = user

    def send(self, message: str, title: Optional[str] = None, priority: Optional[PRIORITY] = None, tags: Optional[str] = None, 
            click: Optional[str] = None, attach: Optional[NTFYUrlAttachment] = None, actions: Optional[Sequence[NTFYAction]] = None, 
            email: Optional[str] = None, delay: Optional[str] = None, icon: Optional[str] = None) -> Response: 
        """
        Parameters
        ----------
        message: :class:`str`
            message's content
        title: Optional[:class:`str`]
            message's title
        priority: Optional[:class:`PRIORITY`]
            message's priority
        tags: Optional[Sequence[:class:`str`]]
            message's tags
        click: Optional[:class:`str`]
            message's click url
        attach: Optional[:class:`NTFYUrlAttachment`]
            message's url attachment
        actions: Optional[Sequence[:class:`NTFYAction`]]
            message's actions
        email: Optional[:class:`str`]
            message's email 
        delay: Optional[:class:`str`]
            message's delay
        icon: Optional[:class:`str`]
            message's icon url

        Returns
        -------
        requests.Response
        """
        auth = self.user.auth() if self.user is not None else None
        return raw_send(self.server.url, self.topic, message, auth = auth, title = title, priority = priority, tags = tags, click = click, attach = attach, actions = actions, email = email, delay = delay, icon = icon)
        
    def send_message(self, message: NTFYPushMessage) -> Response:
        """
        Parameters
        ----------
        message: :class:`NTFYPushMessage`
            message to send
        """
        auth = self.user.auth() if self.user is not None else None
        return raw_send_message(self.server.url, self.topic, message, auth = auth)
        
    async def subscribe(self, handler: Callable[[NTFYMessage], None] = print):
        """
        Parameters
        ----------
        handler: Callable[[:class:`NTFYMessage`], ``None``]
            function to handle printing of received messages; by default it's :py:func:`print`
        """
        auth = self.user.auth() if self.user is not None else None
        await raw_subscribe(self.server.url, self.topic, auth = auth, handler = handler)
