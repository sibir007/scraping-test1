from pathlib import Path
from typing import Any, Iterable
import scrapy
from scrapy.http import Response

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    
    #shortcut for start_requests()
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        # "https://quotes.toscrape.com/page/2/",
    ]
    
    # def start_requests(self) -> Iterable[scrapy.Request]:
    #     urls = [
    #         "https://quotes.toscrape.com/page/1/",
    #         "https://quotes.toscrape.com/page/2/",
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    #     # return super().start_requests()

    # def parse(self, response: Response, **kwargs: Any) -> Any:
    #     page = response.url.split('/')[-2]
    #     file_name = f'quotes-{page}.html'
    #     Path(file_name).write_bytes(response.body)
    #     self.log(f'Saved file {file_name}')
    #     # return super().parse(response, **kwargs)
    def parse(self, response: Response, **kwargs: Any) -> Any:
        for quote in response.xpath('//div[contains(@class, "quote")]'):
            yield {
                'text': quote.xpath('.//span[contains(@class, "text")]/text()').get(),
                'author': quote.xpath('.//small[contains(@class, "author")]/text()').get(),
                'tags': quote.xpath('.//a[contains(@class, "tag")]/text()').getall(),
            }
        # return super().parse(response, **kwargs)
    # def parse(self, response):
    #     for quote in response.css("div.quote"):
    #         yield {
    #             "text": type(quote.css("span.text::text").get()),
    #             "author": type(quote.css("small.author::text").get()),
    #             "tags": type(quote.css("div.tags a.tag::text").getall()),
            # }
        next_page = response.xpath('//li[contains(@class, "next")]/a/@href').get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)