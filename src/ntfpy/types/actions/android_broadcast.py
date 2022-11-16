from .action import NTFYAction
from typing import Optional, MutableMapping

__all__ = [
	"NTFYBroadcastAction"
]

class NTFYBroadcastAction(NTFYAction):
	def __init__(self, label: str):
		super().__init__('broadcast', label)
		self.intent: Optional[str] = None
		self.extras: Optional[MutableMapping[str,str]] = None
	
	def addExtra(self, name: str, value: str):
		if self.extras is None:
			self.extras = {}
		self.extras[name] = value
	
	def format_header(self) -> str:
		res = [self.action, self.label]
		if self.intent is not None:
			res.append(f"intent={self.intent}")
		if self.extras is not None and len(self.extras) > 0:
			res.extend(f"extras.{name}={value}" for name, value in self.extras.items())
		if self.clear is not None:
			res.append(f"clear={'true' if self.clear else 'false'}")
		return ", ".join(res)
