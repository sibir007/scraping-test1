import scrapy
from scrapy.crawler import CrawlerProcess

class RunFromScriptSpider(scrapy.Spider):
    # Your function definitions
    # ....
    pass

process = CrawlerProcess(
    settings=
    'FEEDS': {
        'items.json': {'format': 'json'}
    }
)

process.crawl(RunFromScriptSpider)
process.start() # the script will block here until the crawling is finished


