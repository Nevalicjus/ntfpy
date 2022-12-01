from typing import Final

__all__ = [
    "NTFYServer"
]

class NTFYServer():
    """
    Attributes
    ----------
    url: :class:`str`
        server's url
    """
    def __init__(self, url: str):
        self.url: Final[str] = url
