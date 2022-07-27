import requests
import base64
import json

from .classes import NTFYMessage

__all__ = [
    "raw_subscribe"
]

async def raw_subscribe(server, topic, auth = None):
    if auth is None:
        r = requests.get(f"{server}/{topic}/json", stream = True)
    else:
        auth_bytes = auth.encode("ascii")
        b64_bytes = base64.b64encode(auth_bytes)
        b64_s = b64_bytes.decode("ascii")
        headers = {
            "Authorization": f"Basic {b64_s}"
        }
        r = requests.get(f"{server}/{topic}/json", stream = True, headers = headers)
        for l in r.iter_lines():
            if l:
                d = json.loads(l.decode("utf-8"))
                if d["event"] == "message":
                    m = NTFYMessage(d["message"], d["id"], d["time"], d["topic"])
                    for x in ["title", "priority", "tags", "click", "attach", "actions", "email", "delay"]:
                        if x in d:
                            setattr(m, x, d[x])
                    print(m)
                else:
                    print(d)
