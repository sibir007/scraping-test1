import json
from pathlib import Path

from scrapy import Spider, Request
from scrapy_playwright.page import PageMethod


class HeadersSpider(Spider):
    """Control how requests headers are handled via the PLAYWRIGHT_PROCESS_REQUEST_HEADERS setting.

    If PLAYWRIGHT_PROCESS_REQUEST_HEADERS=None, neither USER_AGENT nor cookies will be sent to the
    website, comment out PLAYWRIGHT_PROCESS_REQUEST_HEADERS to sent them.
    """

    name = "headers"
    custom_settings = {
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            # "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "PLAYWRIGHT_PROCESS_REQUEST_HEADERS": None,
        "USER_AGENT": "Overridden user agent",
    }

    def start_requests(self):
        yield Request(
            url="https://httpbin.org/headers",
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod(
                        "screenshot", path=Path(__file__).parent / "headers.png", full_page=True
                    ),
                ],
            },
            cookies={"foo": "bar"},
        )

    def parse(self, response, **kwargs):
        headers = json.loads(response.css("pre::text").get())["headers"]
        yield {"url": response.url, "headers": headers}


if __name__ == '__main__':
    # import scrapy
    # from scrapy.crawler import CrawlerProcess
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import get_project_settings

    process = CrawlerProcess()

    # 'followall' is the name of one of the spiders of the project.
    process.crawl(HeadersSpider)
    process.start()  # the script will block here until the crawling is finished
