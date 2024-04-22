from typing import Iterable
import scrapy


class MySpyder(scrapy.Spider):
    name = 'myspyder'
    
    def start_requests(self) -> Iterable[Request]:
        return [
            scrapy.FormRequest(
            formdata={'user': 'dima', 'pass': 'secret'},
            callback=self.logged_in,
            )
        ]
        
    def logged_in(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        pass