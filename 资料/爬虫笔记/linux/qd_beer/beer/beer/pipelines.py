# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime

class BeerPipeline(object):
    def process_item(self, item, spider):
        #urcnow()是获取UTC时间
        item['crawled'] = datetime.utcnow()
        #爬虫名
        item['spider'] = spider.name

        return item
