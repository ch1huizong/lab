#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 同一个进程同时运行多个爬虫

from twisted.internet import reactor

import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner(get_project_settings())

runner.crawl('quotes')
runner.crawl('author')
d = runner.join()
d.addBoth(lambda _: reactor.stop())

reactor.run()
