import requests
import os

file_path = 'content' + os.sep

link1 = 'https://www.samsclub.com/robots.txt'
link2 = 'https://www.samsclub.com/sitemap.xml'

resp1 = requests.get(link1)
resp2 = requests.get(link2)

with open(file_path + 'robot.txt', 'wb') as f:
    f.write(resp1.content)

with open(file_path + 'sitmap.xml', 'wb') as f:
    f.write(resp2.content)
    
# print(resp1.text)
# print(resp2.text)
print(resp2.headers['Content-Type'])

