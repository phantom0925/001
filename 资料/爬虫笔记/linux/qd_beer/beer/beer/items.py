# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BeerItem(scrapy.Item):
    
    #标题
    title = scrapy.Field()
    #副标题
    subtitle = scrapy.Field()
    #价格
    price = scrapy.Field()
    #促销价
    promotion_price = scrapy.Field()
    #销量
    sellCount = scrapy.Field()
    #产品信息
    product_info = scrapy.Field()
    #总评论
    commentCount = scrapy.Field()
    #评价细分
    comment = scrapy.Field()

