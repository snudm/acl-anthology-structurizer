#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader

from crawler.items import Paper
import crawler.settings as settings


JOURNAL_IDS = {
    "ACL": "P"
}

year_ids = [str(y)[-2:] for y in range(settings.YEARS[0], settings.YEARS[1])]
journal_id = JOURNAL_IDS[settings.JOURNAL]


class AclSpider(Spider):
    name = "acl"
    allowed_domains = ["aclweb.org"]
    start_urls = ["http://www.aclweb.org/anthology/{0}/{0}{1}/".format(journal_id, year_id)
                  for year_id in year_ids]

    def parse(self, response):
        sel = Selector(response)
        papers = sel.xpath('//div[@id="content"]//p')

        items = []
        for paper in papers:
            l = ItemLoader(item=Paper(), response=response)
            l.add_value('id', paper.xpath('a[1]/text()').extract())
            l.add_value('authors', paper.xpath('b/text()').extract())
            l.add_value('files', paper.xpath('a/@href').extract())
            l.add_value('title', paper.xpath('i/text()').extract())
            items.append(l.load_item())

        return items
