from typing import Optional, Literal, Sequence, MutableSequence, Mapping, Any

from .actions import NTFYAction
from .attachments import NTFYUrlAttachment

__all__ = [
    "NTFYPushMessage",
    "PRIORITY"
]

PRIORITY = Literal[1, 2, 3, 4, 5]

class NTFYPushMessage():
    def __init__(self, message: str, title: Optional[str] = None, priority: Optional[PRIORITY] = None, 
                       tags: Optional[Sequence[str]] = None, click_url: Optional[str] = None, attach: Optional[NTFYUrlAttachment] = None, 
                       actions: Optional[Sequence[NTFYAction]] = None, email: Optional[str] = None, delay: Optional[str] = None,
                       icon_url: Optional[str] = None):
        self.message: str = message
        self.title: Optional[str] = title
        self.priority: Optional[PRIORITY] = priority
        self.tags: Optional[MutableSequence[str]] = list(tags) if tags is not None else None
        self.click_url: Optional[str] = click_url
        self.attachment: Optional[NTFYUrlAttachment] = attach
        self.actions: Optional[MutableSequence[NTFYAction]] = list(actions) if actions is not None else None
        self.email: Optional[str] = email
        self.delay: Optional[str] = delay
        self.icon_url: Optional[str] = icon_url
    
    def addTag(self, tag: str):
        if self.tags is None:
            self.tags = []
        self.tags.append(tag)
    
    def addAction(self, action: NTFYAction):
        if self.actions is None:
            self.actions = []
        self.actions.append(action)
    
    def json(self, topic: str) -> Mapping[str,Any]:
        res: dict[str,Any] = {
            "topic":   topic,
            "message": self.message
        }
        if self.title is not None:
            res["title"] = self.title
        if self.tags is not None:
            res["tags"] = self.tags
        if self.priority is not None:
            res["priority"] = self.priority
        if self.click_url is not None:
            res["click"] = self.click_url
        if self.attachment is not None:
            res.update(self.attachment.format_json())
        if self.actions is not None:
            res["actions"] = [action.format_json() for action in self.actions]
        if self.email is not None:
            res["email"] = self.email
        if self.icon_url is not None:
            res["icon"] = self.icon_url
        if self.delay is not None:
            res["delay"] = self.delay
        return res
    