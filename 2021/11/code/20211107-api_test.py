import requests
url="https://some-random-api.ml/facts/bird"
response=requests.get(url)
data=response.json()
print(data['fact'])