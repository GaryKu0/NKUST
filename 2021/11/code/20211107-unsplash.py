#get random image from unsplash api
#import all required modules
import requests
import json
import random
import os
Access_key="_KJkGKPGR3vzXMHKJTxj6UYfgzEydJ7MsyYBrlyBjSI"
Secret_key="5vFgAc7vx9ev5GKfsPJf46HY9ZPYYvUSMOiUOFp3egI"
#request from unsplash api
url="https://api.unsplash.com/photos/random?client_id="+Access_key
#get the response
response=requests.get(url)
#get the json data
data=response.json()
#get the image url
image_url=data["urls"]["regular"]
#print the image url
print(image_url)

