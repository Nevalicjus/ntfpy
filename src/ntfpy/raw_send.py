import requests
import base64
import json
from typing import Optional, Mapping, Sequence

from .types.push_message import NTFYPushMessage, PRIORITY
from .types.actions      import NTFYAction
from .types.attachments  import NTFYUrlAttachment

__all__ = [
    "raw_send",
    "raw_send_message"
]

def raw_send(server: str, topic: str, message: str, auth: Optional[str] = None, title: Optional[str] = None, 
             priority: Optional[PRIORITY] = None, tags: Optional[Sequence[str]] = None, click: Optional[str] = None, 
             attach: Optional[NTFYUrlAttachment] = None, actions: Optional[Sequence[NTFYAction]] = None, 
             email: Optional[str] = None, delay: Optional[str] = None, icon: Optional[str] = None) -> requests.Response:
    msg = NTFYPushMessage(message, tags = tags, actions = actions)
    msg.title      = title
    msg.priority   = priority
    msg.click_url  = click
    msg.attachment = attach
    msg.email      = email
    msg.delay      = delay
    msg.icon_url   = icon
    return raw_send_message(server, topic, msg, auth = auth)

def raw_send_message(server: str, topic: str, message: NTFYPushMessage, auth: Optional[str] = None) -> requests.Response:
    headers: Mapping[str, str] = {}
    if auth is not None:
        headers["Authorization"] = f"Basic {base64.b64encode(auth.encode('ascii')).decode('ascii')}"
    data = message.json(topic)
    return requests.post(f"{server}/", headers = headers, json = data)
