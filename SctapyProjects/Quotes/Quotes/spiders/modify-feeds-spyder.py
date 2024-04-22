import scrapy
from scrapy.settings import BaseSettings

class MySpyder(scrapy.Spider):
    name = 'myspyder'
    custom_feed = {
         "/home/user/documents/items.json": {
            "format": "json",
            "indent": 4,
        }
    }
    
    @classmethod
    def update_settings(cls, settings: BaseSettings) -> None:
        super().update_settings(settings)
        settings.setdefault('FEEDS', {}).update(cls.custom_feed)

    
    