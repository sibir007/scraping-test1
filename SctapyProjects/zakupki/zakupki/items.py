# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class Purchase(Item):
    fz = Field() # top__title .//div[contains(@class, "registry-entry__header-top__title")]/text()
    reg_num = Field() # .//div[contains(@class, "registry-entry__header-mid__number")]/a/text()
    stage = Field() # .//div[contains(@class, "registry-entry__header-mid__title")]/text()
    p_object = Field() # .//div[contains(@class, "registry-entry__body-value")]/text()
    customer = Field() #
