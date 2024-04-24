# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.spiders import Spider
from .items import Purchase
from scrapy.crawler import Crawler
import re
from urllib.parse import urljoin

class ZakupkiCleanValuePipeline:
    
    rk = re.compile('\s+')
    
    def process_item(self, item: Purchase, spider: Spider):
        # must either: return an item object, 
        # return a Deferred 
        # or raise a DropItem exception.
        adapter = ItemAdapter(item)
        keys = adapter.keys()
        for key in keys:
            if adapter[key]:
                adapter[key] = self._clean_value(adapter[key]) 
        return item
    
    def open_spider(self, spider: Spider):
        pass
    
    def close_spider(self, spider: Spider):
        pass
    
    @classmethod
    def from_crawler(cls, crawler: Crawler):
        return cls()
    
    def _clean_value(self, value: str) -> str:
        """clean string value

        Args:
            value (str): item`s value

        Returns:
            str: cleaned value
        """
        return self.rk.sub(' ', value).strip()
    
class ZakupkiCleanValuePipeline:
    
    rk = re.compile('\s+')
    
    def process_item(self, item: Purchase, spider: Spider):
        # must either: return an item object, 
        # return a Deferred 
        # or raise a DropItem exception.
        adapter = ItemAdapter(item)
        keys = adapter.keys()
        for key in keys:
            if adapter[key]:
                adapter[key] = self._clean_value(adapter[key]) 
        return item
    
    def open_spider(self, spider: Spider):
        pass
    
    def close_spider(self, spider: Spider):
        pass
    
    @classmethod
    def from_crawler(cls, crawler: Crawler):
        return cls()
    
    def _clean_value(self, value: str) -> str:
        """clean string value

        Args:
            value (str): item`s value

        Returns:
            str: cleaned value
        """
        return self.rk.sub(' ', value).strip()
        

# class ZakupkiAbsolutUrlsPeipeline:
    
#     def process_item(self, item: Purchase, spider: Spider):
#         adapter = ItemAdapter(item)
#         url = adapter.get('url')
#         adapter['reg_num_href'] = urljoin(url, adapter['reg_num_href'])
#         return item
   
# class ZakupkiRemoveNotUsedPeipeline:
    
#     def process_item(self, item: Purchase, spider: Spider):
#         adapter = ItemAdapter(item)
#         del adapter['url']
#         return item        
