# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MtimeItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()

    rank = scrapy.Field()
    title = scrapy.Field()
    year = scrapy.Field()
    director = scrapy.Field()
    actors = scrapy.Field()
    categories = scrapy.Field()
    description = scrapy.Field()
    points = scrapy.Field()
    comments = scrapy.Field()
