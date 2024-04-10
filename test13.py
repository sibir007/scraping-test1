import lxml
import lxml.html
from lxml.html import HtmlElement


targerts = ['title', 'price', 'availability', 'imageUrl', 'rating']

musicUrl = "http://books.toscrape.com/catalogue/category/books/music_14/index.html"

doc: HtmlElement = lxml.html.parse(musicUrl)

xPaths = {
  # 'title': '//*[@class="product_pod"]/div[1]/div/div/div/section/div[2]/ol/li[1]/article/h3/a'
  'article': '//*[@class="product_pod"]',
  'title': '/h3/a'

}
doc.find
prod_list = doc.xpath(xPaths['article'])

item: HtmlElement
for item in prod_list:
  title = item[2][0].get('title')
  price = item[3][0].text
  aviailabiity
  print(title, price)