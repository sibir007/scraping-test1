import requests
import json

pageUrl = 'http://httpbin.org/forms/post'
postUrl = 'http://httpbin.org/post'

params = {
    'custname':'Mr. ABC',
    'custtel':'',
    'custemail':'abc@somedomain.com',
    'size':'small',
    'topping':['cheese','mushroom'],
    'delivery':'13:00','comments':'None'
    }

headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Content-Type':'application/x-www-form-urlencoded',
    'Referer':pageUrl
    }

# try:
# except:
js_resp = requests.post(postUrl, params=params, headers=headers).json()

print(json.dumps(js_resp, indent=2))