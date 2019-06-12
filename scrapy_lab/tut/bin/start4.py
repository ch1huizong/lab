#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 顺序爬取

from twisted.internet import reactor, defer

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

configure_logging()
runner = CrawlerRunner(get_project_settings())


@defer.inlineCallbacks
def crawl():
    yield runner.crawl('quotes')
    yield runner.crawl('author')
    reactor.stop()

crawl()
reactor.run()
