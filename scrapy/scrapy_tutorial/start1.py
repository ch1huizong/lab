#! /usr/bin/env python
# -*- coding:UTF-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


process = CrawlerProcess(get_project_settings())  # 会开启一个reactor

process.crawl('quotes')
process.start()
