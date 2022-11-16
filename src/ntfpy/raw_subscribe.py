import requests
import base64
import json
import logging
from typing import Optional, Callable

from .types import NTFYMessage

__all__ = [
    "raw_subscribe"
]

logger = logging.getLogger(__name__)

OPTIONAL_FIELDS = ["title", "priority", "tags", "click", "attach", "actions", "email", "delay"]

async def raw_subscribe(server: str, topic: str, auth: Optional[str] = None, consumer: Callable[[NTFYMessage],None] = print):
    headers = {}
    if auth is not None:
        auth_bytes = auth.encode("ascii")
        b64_bytes = base64.b64encode(auth_bytes)
        b64_s = b64_bytes.decode("ascii")
        headers["Authorization"] = f"Basic {b64_s}"
    r = requests.get(f"{server}/{topic}/json", stream = True, headers = headers)
    for l in r.iter_lines():
        if l:
            d = json.loads(l.decode("utf-8"))
            if d["event"] == "message":
                m = NTFYMessage(d["message"], d["id"], d["time"], d["topic"])
                for x in OPTIONAL_FIELDS:
                    if x in d:
                        setattr(m, x, d[x])
                consumer(m)
            else:
                logger.debug(d)
