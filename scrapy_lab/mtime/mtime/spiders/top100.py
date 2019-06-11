# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from mtime.items import MtimeItem
from mtime.loaders import MtimeLoader


class Top100Spider(scrapy.Spider):
    name = 'top100'
    allowed_domains = ['mtime.com']
    start_urls = [
        'http://www.mtime.com/top/movie/top100/',
    ]

    def parse(self, response):
        for movie in response.css('div.top_list ul li'):
            movie_loader = MtimeLoader(item=MtimeItem(), selector=movie)
            movie_loader.add_css('rank', 'div.number em::text')
            movie_loader.add_css('image_urls', 'div.mov_pic a img::attr(src)')
            movie_loader.add_css('title', 'div.mov_con h2 a::text')
            movie_loader.add_xpath('director', './/p[contains(text(), "导演")]/a/text()')
            movie_loader.add_xpath('actors', './/p[contains(text(), "主演")]/a/text()')
            movie_loader.add_xpath('categories', './/p[contains(text(), "类型")]//a/text()')
            movie_loader.add_css('description','div.mov_con p.mt3::text')
            movie_loader.add_css('points', 'div.mov_point b.point span::text')
            movie_loader.add_css('comments', 'div.mov_point b.point + p::text')
            yield movie_loader.load_item()

        for next_page in response.css('div#PageNavigator a.num'):
            yield response.follow(next_page, callback=self.parse)
