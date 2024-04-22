#from commnd line:
# scrapy crawl accessargspider -a category=electronics


from typing import Any, Iterable

import scrapy

class AccessArgSpider(scrapy.Spider):
    name = 'accessargspider'
    
    def __init__(self, name: str | None = None, category=None, **kwargs: Any):
        super().__init__(name, **kwargs)
        self.start_urls = [f'https://www.example.com/categories/{category}']
        # ...
        
#The default __init__ method will take any spider arguments and copy them to the 
# spider as attributes. The above example can also be written as follows:        

class AccessArgSpider(scrapy.Spider):
    name = 'accessargspider'
    
    def start_requests(self) -> Iterable[Request]:
        yield scrapy.Request(f'https://www.example.com/categories/{self.category}')