from typing import Any, Mapping, MutableMapping, Optional

from .action import NTFYAction

__all__ = [
	"NTFYBroadcastAction"
]

class NTFYBroadcastAction(NTFYAction):
	def __init__(self, label: str):
		super().__init__("broadcast", label)
		self.intent: Optional[str] = None
		self.extras: Optional[MutableMapping[str, str]] = None
	
	def addExtra(self, name: str, value: str):
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
