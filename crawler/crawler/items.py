# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst


def splitstr(string, delim=';'):
    return [s.strip() for s in string.split(delim)]

class Paper(Item):

    id = Field(output_processor=TakeFirst())
    authors = Field(input_processor=MapCompose(splitstr))
    files = Field()
    title = Field(output_processor=Join())
