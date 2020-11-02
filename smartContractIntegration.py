import requests
import json

url = 'http://localhost:3000/'

response = requests.get(url)
if response.ok:
    jData = json.loads(response.content)
    print(jData)