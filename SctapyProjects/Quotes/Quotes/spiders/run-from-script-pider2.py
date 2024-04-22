# исполняется из рот дирректории проекта

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


process = CrawlerProcess(get_project_settings())
# stop-spider - spider name
process.crawl('stop-spider')
process.start()