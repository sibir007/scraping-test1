from typing import Any, Iterable
import scrapy
from scrapy.http import Response
from scrapy import Request

class MyltiSpider2(scrapy.Spider):
    name = 'myltispider2'
    
    allowed_domains = ['example.com']

    def start_requests(self) -> Iterable[Request]:
        yield scrapy.Request("http://www.example.com/1.html", self.parse)
        yield scrapy.Request("http://www.example.com/2.html", self.parse)
        yield scrapy.Request("http://www.example.com/3.html", self.parse)

    def parse(self, response: Response, **kwargs: Any) -> Any:
        for h3 in response.xpath('//h3').getall():
            yield {'title': h3}
        
        for href in response.xpath('//a/@href').getall():
            yield scrapy.Request(response.urljoin(href), self.parse)
            