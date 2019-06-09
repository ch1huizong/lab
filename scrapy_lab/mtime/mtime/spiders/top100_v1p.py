#! /usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from mtime.items import MtimeItem


class Top100Spider(CrawlSpider):
    name = 'top100'
    allowed_domains = ['mtime.com']
    start_urls = ['http://www.mtime.com/top/movie/top100']

    rules = (
        Rule(LinkExtractor(allow=[r'movie/top100', r'index']), 
            callback='parse_movie', follow=True),
    )
    def parse_movie(self, response):
        for movie in response.css('div.top_list ul li'):
            number = movie.css('div.number em::text').extract_first()
            image_urls = movie.css('div.mov_pic a img::attr(src)').extract()

            title = movie.css('div.mov_con h2 a::text').extract_first()
            year = movie.css('div.mov_con h2 a::text').re_first(r'.*?\((\d+)\)')
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
