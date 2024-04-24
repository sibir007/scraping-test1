import scrapy


class MydomainSpider(scrapy.Spider):
    name = "mydomain"
    allowed_domains = ["mydomanain.com"]
    start_urls = ["https://mydomanain.com"]

    def parse(self, response):
        pass
