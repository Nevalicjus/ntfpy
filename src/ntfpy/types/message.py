import time
from typing import Optional, Sequence

__all__ = [
	"NTFYMessage"
]

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

class NTFYMessage():
    def __init__(self, message: str, id: str, timestamp: int, topic: str, title: Optional[str] = None, 
                       priority: Optional[int] = None, tags: Optional[Sequence[str]] = None, click: Optional[str] = None, 
                       attach = None, actions = None, email: Optional[str] = None, delay = None):
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
    
    def __str__(self):
        return f"{self.id} @ {time.strftime(DATE_FORMAT, time.localtime(self.timestamp))}\n{self.topic}: {self.message}"
