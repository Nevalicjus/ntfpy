from typing import Final

__all__ = [
    "NTFYUser"
]

class NTFYUser():
    """
    Attributes
    ----------
    username: :class:`str`
        user's username
    password: :class:`str`
        user's password
    """
    def __init__(self, username: str, password: str):
        self.username: Final[str] = username
        self.password: Final[str] = password
    
    def auth(self) -> str:
        """
        Returns a ``username:password`` string
        """
        return f"{self.username}:{self.password}"
