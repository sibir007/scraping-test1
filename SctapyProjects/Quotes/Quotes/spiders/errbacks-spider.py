from typing import Any, Iterable
import scrapy
from scrapy import Request
from scrapy.http import Response
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
from twisted.python.failure import Failure


class ErrbackSpider(scrapy.Spider):
    name = 'errback_example'
    start_url = [
        "http://www.httpbin.org/",  # HTTP 200 expected
        "http://www.httpbin.org/status/404",  # Not found error
        "http://www.httpbin.org/status/500",  # server issue
        "http://www.httpbin.org:12345/",  # non-responding host, timeout expected
        "https://example.invalid/",  # DNS error expected
    ]
    
    def start_requests(self) -> Iterable[Request]:
        for url in self.start_urls:
            yield Request(
                url,
                callback=self.parse_httpbin,
                errback=self.errback_httpbin,
                dont_filter=True,
            )
    
    def parse_httpbin(self, response: Response):
        self.logger.info('Got succesful response from {}'.format(response.url))
        # do something useful here...
        request = Request(
            url="http://www.example.com/index.html",
            callback=self.errback_page2,
            errback=self.errback_page2,
            cb_kwargs=dict(main_url=response.url),
            )
        yield request
        
    def errback_httpbin(self, failure: Failure):
        #log all filures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:
        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error("HttpError on %s", response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error("DNSLookupError on %s", request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error("TimeoutError on %s", request.url)
        

    def parse_page2(self, response: Response, **kwargs: Any) -> Any:
        pass

    def errback_page2(self, failure: Failure):
        yield dict(
            main_url = failure.request.cb_kwqrgs['main_url']
        )
        # return super().parse(response, **kwargs)