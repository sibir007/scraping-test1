import requests
import json

pageUrl = 'http://httpbin.org/ip'

# try:
# except:
js_resp = requests.get(pageUrl).json()

print(json.dumps(js_resp, indent=2))