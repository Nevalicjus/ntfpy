from typing import Optional, Mapping, Any

__all__ = [
	"NTFYUrlAttachment"
]

class NTFYUrlAttachment:
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
	
