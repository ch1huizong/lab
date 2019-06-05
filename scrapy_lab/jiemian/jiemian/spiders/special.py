# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SpecialSpider(CrawlSpider):
    name = 'special'
    allowed_domains = ['m.jiemian.com']

    def start_requests(self):
        uid = getattr(self, 'uid', None)
        if not uid:
            self.logger.error('请提供分类UID,退出')
            return
        url = 'https://m.jiemian.com/lists/%s_1.html' % uid
        yield scrapy.Request(url)

    rules = (
        Rule(LinkExtractor(allow=r'article/'), callback='parse_article'),
        Rule(LinkExtractor(allow=r'lists/', restrict_css=r'div.pagination'), follow=True),
    )

    def parse_article(self, response):
        self.logger.info('Downloading %s' % response.url)
        title = response.css('h1.article-title::text').get()
        print(title)
