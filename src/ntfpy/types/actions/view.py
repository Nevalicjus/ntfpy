from .action import NTFYAction
from typing import Mapping, Any

__all__ = [
	"NTFYViewAction"
]

class NTFYViewAction(NTFYAction) :
	def __init__(self, label: str, url: str):
		super().__init__("view", label)
		self.url: str = url
	
	def format_header(self) -> str:
		res = [self.action, self.label, self.url]
		if self.clear is not None:
			res.append(f"clear={'true' if self.clear else 'false'}")
		return ", ".join(res)
