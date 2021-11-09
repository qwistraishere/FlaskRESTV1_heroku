import requests
import json

url = "http://127.0.0.1:5000/test"

payload = {
    "username": "bob",
    "password": "asdf"
}

payload = json.dumps(payload)

headers = {
    'Content-Type': 'application/json'
}

resp = requests.post(url, data=payload, headers=headers)

print(resp.text)