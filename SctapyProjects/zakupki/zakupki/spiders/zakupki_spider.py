from typing import Any
import scrapy
from scrapy.http import Response

class ZakupkiSpider(scrapy.Spider):
    name = 'zakupki'
    
    start_urls = [
        'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_50&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&currencyIdGeneral=-1',
    ]
    
    def parse(self, response: Response, **kwargs: Any) -> Any:
        for purchase in response.xpath('//*[contains(@class, "search-registry-entry-block")]'):
            