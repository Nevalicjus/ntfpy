from .action import NTFYAction
from typing import Mapping, Any

__all__ = [
	"NTFYViewAction"
]

class NTFYViewAction(NTFYAction) :
	def __init__(self, label: str, url: str):
		super().__init__("view", label)
		self.url: str = url
	
	def format_json(self) -> Mapping[str,Any]:
		res: dict[str,Any] = {
			"action": self.action,
			"label":  self.label,
			"url":    self.url
		}
		if self.clear is not None:
			res["clear"] = self.clear
		return res
