from typing import Any
import scrapy
from scrapy.http import Response


class MyltiSpider(scrapy.Spider):
    name = 'myltispider'
    
    allowed_domains = ['example.com']
    start_urls = [
        "http://www.example.com/1.html",
        "http://www.example.com/2.html",
        "http://www.example.com/3.html",
    ]
    
    def parse(self, response: Response, **kwargs: Any) -> Any:
        for h3 in response.xpath('//h3').getall():
            yield {'title': h3}
        
        for href in response.xpath('//a/@href').getall():
            yield scrapy.Request(response.urljoin(href), self.parse)
            