#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2018/10/19 11:26:21
# @Author  : che
# @Email   : ch1huizong@gmail.com
# API

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())  # 会开启一个reactor

process.crawl('quotes') # 前提在一个scrapy项目内部
process.crawl('author') 
process.start()
