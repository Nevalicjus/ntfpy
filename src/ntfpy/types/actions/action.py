from abc import ABC, abstractmethod
from typing import Any, Final, Mapping, Optional
__all__ = [
	"NTFYAction"
]

class NTFYAction(ABC) :
    def __init__(self, action: str, label: str):
        self.action: Final[str] = action
        self.label: str = label
        self.clear: Optional[bool] = None
	
    def clearOnClick(self, clear = True):
        self.clear = clear
	
    @abstractmethod
    def format_json(self) -> Mapping[str, Any]:
        pass
