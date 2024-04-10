import requests
link = "https://feeds.citibikenyc.com/stations/stations.json"
r = requests.get(link)
# print(r.headers)

for k,v in r.request.headers.items():
    print(f'{k}: {v}')

# for k,v in r.headers.items():
#     print(f'{k}: {v}')
print(r.encoding)

print(r.history)

rjson = r.json()

for i in range(10):
    print('Station ', rjson['stationBeanList'][i]['stationName'])

    
