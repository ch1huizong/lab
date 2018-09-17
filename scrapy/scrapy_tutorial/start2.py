#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 不会自己开启reactor, 适合已经存在reactor的情形

from twisted.internet import reactor

import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner(get_project_settings())

d = runner.crawl('author')
d.addBoth(lambda _: reactor.stop())
reactor.run()
