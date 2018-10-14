# -*- coding: utf-8 -*-
import scrapy

class RenrenSpider(scrapy.Spider):
    name = "renren"
    allowed_domains = ["renren.com"]
    start_urls = (
        'https://www.lagou.com/zhaopin/Python/2/?filterOption=2',
    )

    cookies = {
    "JSESSIONID":"ABAAABAAAGHAABH507ABFE06E128E8B095C5AF69ED958A7",
    "_ga":"GA1.2.148909248.1536626576",
    "_gid":"GA1.2.1527702521.1536626576", 
    "user_trace_token":"20180911084412-cd14caa5-b55b-11e8-8e26-525400f775ce", 
    "LGUID":"20180911084412-cd14d483-b55b-11e8-8e26-525400f775ce",
    "Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6":"1536626576,1536626622",
    "index_location_city":"%E5%85%A8%E5%9B%BD", 
    "X_HTTP_TOKEN":"c4442dbf902efffbfb78666b329a55f4",
    "_ga":"GA1.3.148909248.1536626576", 
    "TG-TRACK-CODE":"undefined", 
    "ab_test_random_num":"0",
    "Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6":"1536628638",
    "TG-TRACK-CODE":"undefined"
    }

    # 可以重写Spider类的start_requests方法，附带Cookie值，发送POST请求
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url, cookies = self.cookies, callback = self.parse_page)

    # 处理响应内容
    def parse_page(self, response):
        print "===========" + response.url
        with open("deng.html", "w") as filename:
            filename.write(response.body)