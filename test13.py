import lxml
import lxml.html
from lxml.html import HtmlElement
from lxml.etree import Element
import requests
import util
import os


targerts = ['title', 'price', 'availability', 'imageUrl', 'rating']

musicUrl = "http://books.toscrape.com/catalogue/category/books/music_14/index.html"

resp: requests.Response
if (os.environ.get('USERDOMAIN', 'NOT_VZLJOT') == 'VZLJOT'):
  resp = requests.get(musicUrl, proxies=util.VZLJOT_PROXY)
else:
  resp = requests.get(musicUrl)

doc: HtmlElement = lxml.html.document_fromstring(resp.text)

xPaths = {
  # 'title': '//*[@class="product_pod"]/div[1]/div/div/div/section/div[2]/ol/li[1]/article/h3/a'
  'article': '//article[@class="product_pod"]',
  'title': 'h3/a/@title',
  'aviability': 'div[2]/p[2]',
  'price': 'div[2]/p[1]',
  # 'aviailabiity': 

}
# doc.find
prod_list = doc.xpath(xPaths['article'])
titles = doc.xpath('//article[@class="product_pod"]/h3[1]/a[1]/text()')
prices = doc.xpath('//article[@class="product_pod"]/div[2]/p[1]/text()')


for title in prices:
  print(title)
item: HtmlElement
# for item in prod_list:
#   title = item.xpath(xPaths['title'])[0]
#   # title = item[2][0].get('title')
#   price = item.xpath(xPaths['price'])[0].text
#   # price = item[3][0].text
#   # aviailabiity = item[3][1].text_content()
#   aviailabiity = item.xpath(xPaths['aviability'])[0].text_content().strip()
#   # print(title, price)
#   print(title, price, aviailabiity)