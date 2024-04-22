from typing import Any
import scrapy.exceptions
from scrapy.http import Response
import scrapy.signals
from typing_extensions import Self
import scrapy
from scrapy.crawler import Crawler

class StopSpider(scrapy.Spider):
    name = 'stop'
    start_urls = ['https://docs.scrapy.org/en/latst']

    @classmethod
    def from_crawler(cls, crawler: Crawler, *args: Any, **kwargs: Any) -> Self:
        spyder = super().from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(
            spyder.on_byte_received, signal=scrapy.signals.bytes_received
        )
        return spyder 
    
    def parse(self, response: Response, **kwargs: Any) -> Any:
        # 'last_chars' show that the full response was not downloaded
        yield {
            'len': len(response.text),
            'last_chars': response.text[-40:]
            }

    def on_byte_received(self, data, request, spider):
        raise scrapy.exceptions.StopDownload(fail=False)
    
    