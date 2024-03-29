from typing import Any, Mapping, MutableMapping, Optional

from .action import NTFYAction

__all__ = [
	"NTFYBroadcastAction"
]

class NTFYBroadcastAction(NTFYAction):
    """
    Extends :class:`NTFYAction`
    
    Attributes
    ----------
    label: :class:`str`
        action's label
    """
    def __init__(self, label: str):
        super().__init__("broadcast", label)
        self.intent: Optional[str] = None
        self.extras: Optional[MutableMapping[str, str]] = None
	
    def addExtra(self, name: str, value: str):
        """
        Parameters
        ----------
        name: :class:`str`
            name of the extra
        value: :class:`str`
            value of the extra
        """
        if self.extras is None:
            self.extras = {} 
        self.extras[name] = value 
	
    def format_json(self) -> Mapping[str, Any]:
        res: dict[str, Any] = {
            "action": self.action,
            "label": self.label
        }
        for prop in ["intent", "extras", "clear"]:
            if self.__dict__[prop] is not None:
                res[prop] = self.__dict__[prop]
        return res
