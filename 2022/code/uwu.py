import requests
import json

response = requests.get('https://some-random-api.ml/mc?username=k1ssy0u')
if response.status_code == 200:

    aa = response.content.decode('utf-8')
    tmp = json.loads(aa)
    f = open('hi.json','wb')
    aa1 = json.dumps(tmp, indent = 1,ensure_ascii=False).encode('utf-8')
    f.write(aa1)
    f.close()