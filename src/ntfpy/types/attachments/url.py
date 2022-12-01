from typing import Any, Mapping, Optional

__all__ = [
	"NTFYUrlAttachment"
]

class NTFYUrlAttachment:
    """
    Attributes
    ----------
    url: :class:`str`
        attachment's url
    filename: Optional[:class:`str`]
        attachment's filename
    """
    def __init__(self, url: str, filename: Optional[str] = None):
        self.url = url
        self.filename = filename
	
    def format_json(self) -> Mapping[str,Any] :
        res = {
            "attach": self.url
        }
        if self.filename is not None :
            res["filename"] = self.filename
        return res	
