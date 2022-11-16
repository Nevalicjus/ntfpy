from .action import NTFYAction
from typing import Optional, MutableMapping

__all__ = [
	"NTFYHttpAction"
]

class NTFYHttpAction(NTFYAction):
	def __init__(self, label: str, url: str):
		super().__init__('http', label)
		self.url = url
		self.method: Optional[str] = None
		self.headers: Optional[MutableMapping[str,str]] = None
		self.body: Optional[str] = None
	
	def addHeader(self, header: str, value: str):
		if self.headers is None:
			self.headers = {}
		self.headers[header] = value
	
	def format_header(self) -> str:
		res = [self.action, self.label, self.url]
		if self.method is not None:
			res.append(f"method={self.method}")
		if self.headers is not None and len(self.headers) > 0:
			res.extend(f"headers.{name}={value}" for name, value in self.headers.items())
		if self.body is not None:
			res.append(f"body={self.body}")
		if self.clear is not None:
			res.append(f"clear={'true' if self.clear else 'false'}")
		return ", ".join(res)