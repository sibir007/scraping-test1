import requests
link = 'https://www.python.org'
r = requests.get(link)
# print(r.headers)

for k,v in r.request.headers.items():
    print(f'{k}: {v}')

# for k,v in r.headers.items():
#     print(f'{k}: {v}')
print(r.encoding)

print(r.history)
