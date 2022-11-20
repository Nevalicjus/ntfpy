import requests
import base64
import json
import logging
from typing import Optional, Callable

from .types.message import NTFYMessage

__all__ = [
    "raw_subscribe"
]

logger = logging.getLogger(__name__)

OPTIONAL_FIELDS = ["title", "priority", "tags", "click", "attach", "actions", "email", "delay", "icon"]

async def raw_subscribe(server: str, topic: str, auth: Optional[str] = None, handler: Callable[[NTFYMessage], None] = print):
    headers = {}
    if auth is not None:
        headers["Authorization"] = f"Basic {base64.b64encode(auth.encode('ascii')).decode('ascii')}"
    r = requests.get(f"{server}/{topic}/json", stream = True, headers = headers)
    for l in r.iter_lines():
        if l:
            d = json.loads(l.decode("utf-8"))
            if d["event"] == "message":
                m = NTFYMessage(d["message"], d["id"], d["time"], d["topic"])
                for x in OPTIONAL_FIELDS:
                    if x in d:
                        setattr(m, x, d[x])
                handler(m)
            else:
                logger.debug(d)
