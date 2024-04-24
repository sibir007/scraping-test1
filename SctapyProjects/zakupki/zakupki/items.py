# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class Purchase(Item):
    fz = Field() # top__title .//div[contains(@class, "registry-entry__header-top__title")]/text()
    reg_num = Field() # .//div[contains(@class, "registry-entry__header-mid__number")]/a/text()
    reg_num_href = Field() # .//div[contains(@class, "registry-entry__header-mid__number")]/a/@href
    stage = Field() # .//div[contains(@class, "registry-entry__header-mid__title")]/text()
    p_object = Field() # .//div[contains(@class, "registry-entry__body-value")]/text()
    organization_type = Field() # ./div[2]/dev[1]/text()
    organization_name = Field() # .//div[contains(@class, "registry-entry__body-href")]/a/text()
    organization_href = Field() # .//div[contains(@class, "registry-entry__body-href")]/a/@href
    s_price = Field() # .//div[contains(@class, "price-block__value")]/text()
    posted = Field() # .//div[normalize-space(.)="Размещено"]/parent::*/div[2]/text()
    updated = Field() # .//div[normalize-space(.)="Обновлено"]/parent::*/div[2]/text()
    ending = Field() # .//div[normalize-space(.)="Окончание подачи заявок"]/following-sibling::div[1]/text()
    documents_href = Field() # .//a[normalize-space(.)="Документы"]/@href