import requests
import base64
import json
from typing import Optional, Mapping

__all__ = [
    "raw_send"
]

def raw_send(server: str, topic: str, message: str, auth: Optional[str] = None, title: Optional[str] = None, 
             priority: Optional[str] = None, tags: Optional[str] = None, click: Optional[str] = None, 
             attach: Optional[str] = None, actions: Optional[str] = None, email: Optional[str] = None, 
             delay: Optional[str] = None, icon: Optional[str] = None):
    headers: Mapping[str, str] = {}
    data: Mapping[str, str] = {}
    if auth is not None:
        headers["Authorization"] = f"Basic {base64.b64encode(auth.encode('ascii')).decode('ascii')}"
    data["topic"] = topic
    data["message"] = message
    if title is not None:
        data["title"] = title
    if tags is not None:
        data["tags"] = tags
    if priority is not None:
        data["priority"] = priority
    if click is not None:
        data["click"] = click
    if attach is not None:
        data["attach"] = attach
    if actions is not None:
        data["actions"] = actions
    if email is not None:
        data["email"] = email
    if icon is not None:
        data["icon"] = icon
    if delay is not None:
        data["delay"] = delay
    print(data)
    requests.post(f"{server}/", headers = headers, data = json.dumps(data))
