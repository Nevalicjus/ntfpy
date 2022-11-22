from typing import Final

__all__ = [
    "NTFYUser"
]

class NTFYUser():
    def __init__(self, username: str, password: str):
        self.username: Final[str] = username
        self.password: Final[str] = password
    
    def auth(self) -> str:
        return f"{self.username}:{self.password}"
