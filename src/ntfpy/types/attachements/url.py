from typing import Optional

__all__ = [
	"NTFYUrlAttachement"
]

class NTFYUrlAttachement:
	def __init__(self, url: str, filename: Optional[str] = None) :
		self.url = url
		self.filename = filename
	