import requests
import base64
import json

__all__ = (
    'subscribe'
)

async def subscribe(server, topic, auth = None):
    if auth is None:
        r = requests.get(f"{server}/{topic}/json", stream = True)
    else:
        auth_bytes = auth.encode('ascii')
        b64_bytes = base64.b64encode(auth_bytes)
        b64_s = b64_bytes.decode('ascii')
        headers = {
            "Authorization": f"Basic {b64_s}"
        }
        r = requests.get(f"{server}/{topic}/json", stream = True, headers = headers)
        for l in r.iter_lines():
            if l:
                print(json.loads(l.decode('utf-8')))
