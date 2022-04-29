import json
from urllib import response
import requests

data = {
    "text": "hello world",
    "From": "english",
    "to": "chinese"
}
response = requests.get("https://su-api.deta.dev/translate", data)
print(response.text)

domain = {
    'domain': 'sususu.dev'
}
response1 = requests.post("https://su-api.deta.dev/whois/", json=domain)
print(response1.text)

response1=requests.get("https://su-api.deta.dev/amongus/")
#download response.png to local
with open("AmongUs.png", "wb") as f:
    f.write(response1.content)


# response1=requests.post("https://su-api.deta.dev/whois/raw",json=domain)
# print(response1.json())
