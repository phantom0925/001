# coding:utf-8

# -*- coding: utf-8 -*-
import scrapy
import json 
import Queue
import requests
from beer.items import BeerItem
from scrapy.http import Request
from scrapy.dupefilters import RFPDupeFilter
from scrapy_redis.spiders import RedisSpider


class BEerSpider(RedisSpider):
    name = 'b_eer'
    redis_key = 'b_eer:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))

        # 修改这里的类名为当前类名
        super(BEerSpider, self).__init__(*args, **kwargs)

    def parse(self,response):
    	""""""
        print response.request.headers["User-Agent"]
    	js = json.loads(response.body)
    	#解析json数据提取id
        items = js['items']
        #用来存储id
        ids = Queue.Queue()
        for i in items:
            id = i['item_id']
            ids.put(id)
        #拼接url
        while not ids.empty():
                url = 'https://h5api.m.taobao.com/h5/mtop.taobao.detail.getdetail/6.0/?data=%7B"itemNumId"%3A"'+str(ids.get())+'"%7D'
                print "---1---"
                print url
                yield Request(url,callback=self.parse_item)
    
    def parse_item(self,response):
            """"""
            i = BeerItem()

            data = json.loads(response.body)
            data = data["data"]
            Item = data["item"]
            #标题
            i['title'] = Item['title']
            #副标题
            i['subtitle'] = Item['subtitle']
            #解析数据获取价格
            mockData = data['mockData']
            mockData = json.loads(mockData)
            #价格
            i['price'] = mockData["price"]["price"]["priceText"]
            #解析数据用来获取活动价格
            apiStack = data['apiStack']
            for i in apiStack:
                    value = i['value']
            #销量
            value = json.loads(value)
            i['sellCount'] = value['item']['sellCount']
            #促销价
            i['promotion_price'] = value['price']['price']['priceText']

            #解析数据用来获取产品信息
            info = data['props']['groupProps']
            for i in info:
                    info = i
            key = "基本信息"
            key = unicode(key,"utf8")
            #产品信息
            i['product_info'] = info[key]
            #总评价数目
            i['commentCount'] = data['rate']['totalCount']
            #评分细分
            i['comment'] = data['rate']['keywords']
            print "----end---"
            yield i


