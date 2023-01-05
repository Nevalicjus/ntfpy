import requests
import logging
import json
import base64
from typing import Callable, Final, Optional, Sequence

from .server import NTFYServer
from .actions import NTFYAction
from .attachments import NTFYUrlAttachment
from .message import NTFYMessage
from .push_message import NTFYPushMessage, PRIORITY
from .user import NTFYUser

__all__ = [
    "NTFYClient"
]

logger = logging.getLogger(__name__)
OPTIONAL_FIELDS = ["title", "priority", "tags", "click", "attach", "actions", "email", "delay", "icon"]

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
            email: Optional[str] = None, delay: Optional[str] = None, icon: Optional[str] = None) -> requests.Response: 
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
        msg = NTFYPushMessage(message, tags = tags, actions = actions)
        msg.title = title
        msg.priority = priority
        msg.click_url = click
        msg.attachment = attach
        msg.email = email
        msg.delay = delay
        msg.icon_url = icon

        headers: Mapping[str, str] = {}
        if auth is not None:
            headers["Authorization"] = f"Basic {base64.b64encode(auth.encode('ascii')).decode('ascii')}"
        data = msg.json(self.topic)
        return requests.post(f"{self.server.url}/", headers = headers, json = data)
        
    def send_message(self, message: NTFYPushMessage) -> requests.Response:
        """
        Parameters
        ----------
        message: :class:`NTFYPushMessage`
            message to send
        """
        auth = self.user.auth() if self.user is not None else None
        headers: Mapping[str, str] = {}
        if auth is not None:
            headers["Authorization"] = f"Basic {base64.b64encode(auth.encode('ascii')).decode('ascii')}"
        data = message.json(self.topic)
        return requests.post(f"{self.server.url}/", headers = headers, json = data)
        
    async def subscribe(self, handler: Callable[[NTFYMessage], None] = print):
        """
        Parameters
        ----------
        handler: Callable[[:class:`NTFYMessage`], ``None``]
            function to handle printing of received messages; by default it's :py:func:`print`
        """
        auth = self.user.auth() if self.user is not None else None

        headers = {}
        if auth is not None:
            headers["Authorization"] = f"Basic {base64.b64encode(auth.encode('ascii')).decode('ascii')}"
        r = requests.get(f"{self.server}/{self.topic}/json", stream = True, headers = headers)
        for l in r.iter_lines():
            if l:
                d = json.loads(l.decode("utf-8"))
                if d["event"] == "message":
                    m = NTFYMessage(d["message"], d["id"], d["time"], d["topic"])
                    for x in OPTIONAL_FIELDS:
                        if x in d:
                            setattr(m, x, d[x])
                    handler(m)
                else:
                    logger.debug(d)
