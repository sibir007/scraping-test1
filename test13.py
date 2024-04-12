import lxml
from lxml import html
from lxml.html import HtmlElement
from lxml.etree import Element
import requests
import util
import os
from io import BytesIO

targerts = ['title', 'price', 'availability', 'imageUrl', 'rating']

musicUrl = "http://books.toscrape.com/catalogue/category/books/music_14/index.html"

resp: requests.Response
if (os.environ.get('USERDOMAIN', 'NOT_VZLJOT') == 'VZLJOT'):
  resp = requests.get(musicUrl, proxies=util.VZLJOT_PROXY)
else:
  resp = requests.get(musicUrl)

doc_tree  = html.parse(BytesIO(resp.content))
doc_root = doc_tree.getroot()
# doc: HtmlElement = lxml.html.document_fromstring(resp.text)

# xPaths = {
  # 'title': '//*[@class="product_pod"]/div[1]/div/div/div/section/div[2]/ol/li[1]/article/h3/a'
  # 'article': '//article[@class="product_pod"]',
  # 'title': 'h3/a/@title',
  # 'aviability': 'div[2]/p[2]',
  # 'price': 'div[2]/p[1]',
  # 'aviailabiity': 

# }
# doc.find
article = doc_root.xpath('//article[@class="product_pod"]')[1]
titles: list = article.xpath('//h3[1]/a[1]/text()')
prices = article.xpath('//p[contains(@class, "price_color")]/text()[normalize-space()]')
availability = article.xpath('//p[contains(@class, "availability")]/text()[normalize-space()]')
doc_root.make_links_absolute(musicUrl)
imageUrls = article.xpath('//div[@class="image_container"]/a[1]/img[1]/@src')
ratings = article.xpath('//p[contains(@class, "star-rating")]/@class')

def normalise_str(list_str: list) -> list:
  return list(map(lambda list_item: list_item.strip(), list_str))

titles = normalise_str(titles)
prices = normalise_str(prices)
availability = normalise_str(availability)
imageUrls = normalise_str(imageUrls)
ratings = normalise_str(ratings)


articles = list(zip(titles,prices,availability,imageUrls,ratings))

print(articles)

# for title in titles:
#   print(title)
# item: HtmlElement
# for item in prod_list:
#   title = item.xpath(xPaths['title'])[0]
#   # title = item[2][0].get('title')
#   price = item.xpath(xPaths['price'])[0].text
#   # price = item[3][0].text
#   # aviailabiity = item[3][1].text_content()
#   aviailabiity = item.xpath(xPaths['aviability'])[0].text_content().strip()
#   # print(title, price)
#   print(title, price, aviailabiity)