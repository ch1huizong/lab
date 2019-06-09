# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.loader import ItemLoader
from mtime.items import MtimeItem


class Top100Spider(scrapy.Spider):
    name = 'top100'
    allowed_domains = ['mtime.top']
    start_urls = [
        "http://www.mtime.com/top/movie/top100/",
    ]

    def parse(self, response):
        item = ItemLoader(item=Item(), response=response)

        for movie in response.css('div.top_list ul li'):
            number = movie.css('div.number em::text').get()
            image_urls = movie.css('div.mov_pic a img::attr(src)').getall()

            title = movie.css('div.mov_con h2 a::text').get()
            year = title
            director = movie.css('div.mov_con').xpath('p[contains(.,$d)]',
                    d=u'导演').xpath('a/text()').extract()
            actors = movie.css('div.mov_con').xpath('p[contains(.,$a)]',
                    a=u'主演').xpath('a/text()').extract()
            categories = movie.css('div.mov_con').xpath('p[contains(.,$c)]',
                    c=u'类型').xpath('.//a/text()').extract()
            description = movie.css('div.mov_con p.mt3::text').extract_first()
            point = movie.css('div.mov_point b.point span::text').extract()
            comments = movie.css('div.mov_point b.point + p::text').re_first(r'(\d+).*')
            yield MtimeItem(number=number, image_urls=image_urls, title=title, year=year,
                director=director, actors=actors, categories=categories,
                description=description, point=point, comments=comments)
