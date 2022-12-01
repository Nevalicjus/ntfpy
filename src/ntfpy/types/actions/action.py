from abc import ABC, abstractmethod
from typing import Any, Final, Mapping, Optional

__all__ = [
	"NTFYAction"
]

class NTFYAction(ABC):
    """
    Attributes
    ----------
    action: :class:`str`
        action's type
    label: :class:`str`
        action's label
    """
    def __init__(self, action: str, label: str):
        self.action: Final[str] = action
        self.label: str = label
        self.clear: Optional[bool] = None
	
    def clearOnClick(self, clear = True):
        """
        Parameters
        ----------
        clear: :class:`bool`
            whether or not to clear the notification after action button is tapped
        """
        self.clear = clear
	
    @abstractmethod
    def format_json(self) -> Mapping[str, Any]:
        pass
