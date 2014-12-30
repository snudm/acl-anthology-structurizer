# -*- coding: utf-8 -*-

# Modify the values below
YEARS = [1979, 2014] # Start, End
JOURNAL = "ACL"

# Crawler config
BOT_NAME = 'snudm.acl.crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = '%s (+http://dm.snu.ac.kr)' % BOT_NAME
