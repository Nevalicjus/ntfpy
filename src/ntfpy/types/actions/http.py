from typing import Any, Literal, Mapping, MutableMapping, Optional

from .action import NTFYAction

__all__ = [
	"NTFYHttpAction"
]

METHOD = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]

class NTFYHttpAction(NTFYAction):
    """
    Extends :class:`NTFYAction`

    Attributes
    ----------
    label: :class:`str`
        action's label
    url: :class:`str`
        action's url
    """
    def __init__(self, label: str, url: str):
        super().__init__("http", label)
        self.url = url
        self.method: Optional[str] = None
        self.headers: Optional[MutableMapping[str, str]] = None
        self.body: Optional[str] = None
    
    def setMethod(self, method: METHOD):
        """
        Parameters
        ----------
        method: :class:`METHOD`
            method to set
        """
        self.method = method
	
    def addHeader(self, name: str, value: str):
        """
        Parameters
        ----------
        name: :class:`str`
            name of the header
        value: :class:`str`
            value of the header
        """
        if self.headers is None:
            self.headers = {}
        self.headers[name] = value
    
    def format_header(self) -> Mapping[str, Any]:
        res: dict[str, Any] = {
            "action": self.action, 
            "label": self.label,
            "url": self.url
        }
        for prop in ["method", "headers", "body", "clear"]:
            if self.__dict__[prop] is not None:
                res[prop] = self.__dict__[prop]
        return res
