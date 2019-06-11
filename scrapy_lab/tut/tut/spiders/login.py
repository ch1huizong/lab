# -*- coding: utf-8 -*-
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['webscraping.com']
    start_urls = ['http://example.webscraping.com/places/default/user/login']

    def parse(self, response):
            return scrapy.FormRequest.from_response(
                response,
                formdata={
                    'email': 'chehuizong@163.com',
                    'password': 'quiet123'
                },
                callback=self.after_login
            )

    def after_login(self, response):
        # check login succeed before going on
        if response.css('div#pagination').get():
            self.logger.info("Login Success!")
            return

