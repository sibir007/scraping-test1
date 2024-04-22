from typing import Any
import scrapy
from scrapy.http import Response

def authentification_filed(response):
    # TODO: Check the contents of the response and return True if it failed
    # or False if it succeeded.
    pass

class LoginSpider(scrapy.Spider):
    name = 'login_spider'
    start_urls = ["http://www.example.com/users/login.php"]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        yield scrapy.FormRequest.from_response(
            response=response,
            formdata={'username': 'john', 'password': 'secret'},
            callback = self.after_login,
        )
        
    def after_login(self, response):
        if authentification_filed(response):
            self.logger.error('Login failed')
            return