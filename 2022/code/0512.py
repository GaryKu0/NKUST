import json
from urllib import response
import requests

domain = {
    'domain': 'sususu.dev'
}
response1 = requests.post("https://su-api.deta.dev/whois/raw", json=domain)
res=response1.content.decode('utf-8')
tmp=json.loads(res)
#save response.txt to response.json
f=open("response.json","wb")
k=json.dumps(tmp,indent=4,ensure_ascii=False).encode('utf-8')
f.write(k)
f.close()