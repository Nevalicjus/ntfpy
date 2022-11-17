from abc import ABC, abstractmethod
from typing import Optional

__all__ = [
	"NTFYAction"
]

class NTFYAction(ABC) :
    def __init__(self, action: str, label: str):
        self.action = action
        self.label = label
        self.clear: Optional[bool] = None
	
    def clearOnClick(self, clear = True):
        self.clear = clear
	
    @abstractmethod
    def format_header(self) -> str:
        pass
