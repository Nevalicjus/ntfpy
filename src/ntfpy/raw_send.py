import requests
import base64
from typing import Mapping, Optional, Sequence

from .types.actions import NTFYAction
from .types.attachments import NTFYUrlAttachment
from .types.push_message import NTFYPushMessage, PRIORITY

__all__ = [
    "raw_send",
    "raw_send_message"
]

def raw_send(server: str, topic: str, message: str, auth: Optional[str] = None, title: Optional[str] = None, 
             priority: Optional[PRIORITY] = None, tags: Optional[Sequence[str]] = None, click: Optional[str] = None, 
             attach: Optional[NTFYUrlAttachment] = None, actions: Optional[Sequence[NTFYAction]] = None, 
             email: Optional[str] = None, delay: Optional[str] = None, icon: Optional[str] = None) -> requests.Response:
    """
    Internal method for sending messages
    
    Parameters
    ----------
    server: :class:`str`
        server's url address
    topic: :class:`str`
        topic where to send the message to
    message: :class:`str`
        message's content
    auth: Optional[:class:`str`]
        ``user:pass``
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
    """
    msg = NTFYPushMessage(message, tags = tags, actions = actions)
    msg.title = title
    msg.priority = priority
    msg.click_url = click
    msg.attachment = attach
    msg.email = email
    msg.delay = delay
    msg.icon_url = icon
    return raw_send_message(server, topic, msg, auth = auth)

def raw_send_message(server: str, topic: str, message: NTFYPushMessage, auth: Optional[str] = None) -> requests.Response:
    headers: Mapping[str, str] = {}
    if auth is not None:
        headers["Authorization"] = f"Basic {base64.b64encode(auth.encode('ascii')).decode('ascii')}"
    data = message.json(topic)
    return requests.post(f"{server}/", headers = headers, json = data)
