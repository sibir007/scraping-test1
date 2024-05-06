import scrapy


class GovtorgSpider(scrapy.Spider):
    name = "govtorg"
    allowed_domains = ["torgi.gov.ru"]
    start_urls = ["https://torgi.gov.ru"]

    def parse(self, response):
        pass
