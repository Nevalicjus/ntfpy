from typing import Optional, MutableSequence

from .actions import NTFYAction
from .attachments import NTFYUrlAttachment

__all__ = [
	"NTFYPushMessage"
]

class NTFYPushMessage():
    def __init__(self, message: str, title: Optional[str] = None, priority: Optional[int] = None, 
                       tags: Optional[MutableSequence[str]] = None, click_url: Optional[str] = None, attach: Optional[NTFYUrlAttachment] = None, 
                       actions: Optional[MutableSequence[NTFYAction]] = None, email: Optional[str] = None, delay: Optional[str] = None,
                       icon_url: Optional[str] = None):
        self.message = message
        self.title = title
        self.priority = priority
        self.tags = tags
        self.click_url = click_url
        self.attachment = attach
        self.actions = actions
        self.email = email
        self.delay = delay
        self.icon_url = icon_url
    
    def addTag(self, tag: str) :
        if self.tags is None :
            self.tags = []
        self.tags.append(tag)
    
    def addAction(self, action: NTFYAction) :
        if self.actions is None :
            self.actions = []
        self.actions.append(action)
    
