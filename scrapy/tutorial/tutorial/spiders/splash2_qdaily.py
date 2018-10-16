#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2018/09/28 15:51:22
# @Author  : che
# @Email   : ch1huizong@gmail.com

import time

import scrapy
from scrapy_splash import SplashRequest


class QdailySpider(scrapy.Spider):
    name = 'qdaily'

    def start_requests(self):
        url = 'http://www.qdaily.com/categories/categorymore/18/%s.json' 
        url = url % int(time.mktime(time.localtime()))

        splash_args = {
            'html': 1,
            'png': 1,
            'width': 600,
            'render_all': 1,
            'wait': 0.5,  # render_all required
        }

        yield SplashRequest(
                url, 
                self.parse_result,
                endpoint='render.json',
                args=splash_args
        )

    def parse_result(self, response):
        self.logger.info('Get response: %s' % response.url)
        print(response.data)
