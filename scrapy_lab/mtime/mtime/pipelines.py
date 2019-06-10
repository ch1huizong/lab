# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class MtimePipeline(ImagesPipeline):

    def get_media_requests(self, item,info):
        for image_url in item['image_urls']: # may ignore
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok ]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item


class CleanPipeline(object):

    def process_item(self, item, spider):
        if item.get('title'):
            item['year'] = re.findall(r'\((\d+)\)', item['title'])[0]

        if item.get('comments'):
            item['comments'] = re.findall(r'(\d+)', item['comments'])[0]
        print(item)
        return item
