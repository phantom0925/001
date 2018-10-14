# -*- coding: utf-8 -*-
import scrapy


class Denglu21Spider(scrapy.Spider):
    name = "denglu2"
    allowed_domains = ["lagou.com"]

    def start_requests(self):
        url = 'https://passport.lagou.com/login/login.html'
        # FormRequest 是Scrapy发送POST请求的方法
        yield scrapy.FormRequest(
                url = url,
                formdata = {"username" : "18809236315", "password" : "995945908a"},
                callback = self.parse_page)

    def parse_page(self, response):
        with open("mao2.html", "w") as filename:
            filename.write(response.body)