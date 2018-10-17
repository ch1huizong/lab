#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2018/09/28 15:51:22
# @Author  : che
# @Email   : ch1huizong@gmail.com

import scrapy
from scrapy_splash import SplashRequest


class GoogleSpider(scrapy.Spider):
    name = 'google'

    def start_requests(self):
        url = 'https://www.google.com'
        yield SplashRequest(
                url, 
                callback=self.parse, 
                args={'wait': 0.5, 'proxy':'http://192.168.0.2:8100'},
        )

    def parse(self, response):
        self.logger.info('Get response: %s' % response.url)
        #print(response.text)
