import logging

from scrapy import signals, Spider
from scrapy.exceptions import NotConfigured
from scrapy.crawler import Crawler

logger = logging.getLogger(__name__)

class SpiderOpenClosedLogging:
    def __init__(self, item_count) -> None:
        self.item_count = item_count
        self.item_scraped = 0
        
    @classmethod
    def from_crawler(cls, crawler: Crawler):
        # first check if the extension should be enabled and raise
        # NotConfigured otherwise
        if not crawler.settings.getbool('MYEXT_ENABLED'):
            raise NotConfigured
        
        # get the number of items from settings
        item_count = crawler.settings.getint('MYEXT_ITEMCOUNT', 1000)

        # instantiate the extension object
        ext = cls(item_count)

        # connect the extension object to signals
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)
        
    def spider_opened(self, spider: Spider):
        logger.info(f'opened spider {spider.name}')

    def spider_closed(self, spider: Spider):
        logger.info(f'closed spider {spider.name}')
    
    def item_scraped(self, item, spider):
        self.item_scraped += 1
        if self.item_scraped % self.item_count == 0:
            logger.info(f'scraped {self.item_scraped} items')