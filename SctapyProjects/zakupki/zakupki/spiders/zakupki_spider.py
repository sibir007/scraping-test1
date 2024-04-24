from typing import Any
import scrapy
from scrapy.http import Response
from zakupki.zakupki.items import Purchase
from scrapy.loader import ItemLoader

class ZakupkiSpider(scrapy.Spider):
    name = 'zakupki'
    
    start_urls = [
        'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_50&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&currencyIdGeneral=-1',
    ]
    
    def parse(self, response: Response, **kwargs: Any) -> Any:
        for purchase in response.xpath('//div[contains(@class, "search-registry-entry-block")]'):
            p_item = Purchase(
                fz = purchase.xpath('.//div[contains(@class, "registry-entry__header-top__title")]/text()').get(),
                reg_num = purchase.xpath('.//div[contains(@class, "registry-entry__header-mid__number")]/a/text()').get(),
                reg_num_href = purchase.xpath('.//div[contains(@class, "registry-entry__header-mid__number")]/a/@href').get(),
            )
            
            # l = ItemLoader(item=Purchase(), response=purchase)
            # l.add_xpath('fz', './/div[contains(@class, "registry-entry__header-top__title")]/text()')
            # l.add_xpath('')