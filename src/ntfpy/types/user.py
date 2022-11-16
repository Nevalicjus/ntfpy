
__all__ = [
    "NTFYUser"
]

class NTFYUser():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def auth(self) -> str :
        return f"{self.username}:{self.password}"