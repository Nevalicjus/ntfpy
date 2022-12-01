import time
from typing import Any, Optional, Sequence

__all__ = [
	"NTFYMessage"
]

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

class NTFYMessage():
    """
    Attributes
    -----------
    message: :class:`str`
        message's content
    id: :class:`int`
        message's id
    timestamp: :class:`int`
        message's timestamp (unix)
    topic: :class:`str`
        message's topic
    title: Optional[:class:`str`]
        message's title
    priority: Optional[:class:`int`]
        message's priority
    tags: Optional[Sequence[:class:`str`]]
        message's tags
    click: Optional[:class:`str`]
        message's click url
    attach: Optional[``Any``]
        message's attachments
    actions: Optional[``Any``]
        message's actions
    email: Optional[:class:`str`]
        message's email
    delay: Optional[:class:`str`]
        message's delay
    icon: Optional[:class:`str`]
        message's icon
    """
    def __init__(self, message: str, id: str, timestamp: int, topic: str, title: Optional[str] = None, 
                       priority: Optional[int] = None, tags: Optional[Sequence[str]] = None, click: Optional[str] = None, 
                       attach: Optional[Any] = None, actions: Optional[Any] = None, email: Optional[str] = None, delay: Optional[str] = None,
                       icon: Optional[str] = None):
        self.message = message
        self.id = id
        self.timestamp = timestamp
        self.topic = topic
        self.title = title
        self.priority = priority
        self.tags = tags
        self.click = click
        self.attach = attach
        self.actions = actions
        self.email = email
        self.delay = delay
        self.icon = icon
    
    def __str__(self):
        return f"{self.id} @ {time.strftime(DATE_FORMAT, time.localtime(self.timestamp))}\n{self.topic}: {self.message}"
