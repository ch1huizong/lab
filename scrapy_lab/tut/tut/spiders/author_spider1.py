# -*- coding: utf-8 -*-
# 链接爬虫

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AuthorSpiderCrawlSpider(CrawlSpider):
    name = "author1"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(allow=r"/author/"), callback="parse_author"),
        Rule(LinkExtractor(allow=r"/page/", deny=r"/tag/")),
    )

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            "name": extract_with_css("h3.author-title::text"),
            "birthdate": extract_with_css(".author-born-date::text"),
            "bio": extract_with_css(".author-description::text"),
        }
