# -*- coding: utf-8 -*-
import scrapy



class Denglu3Spider(scrapy.Spider):
    name = "denglu3"
    allowed_domains = ["lagou.com"]
    start_urls = (
        "https://passport.lagou.com/login/login.html",
    )

    # 处理start_urls里的登录url的响应内容，提取登陆需要的参数（如果需要的话)
    def parse(self, response):
        # 提取登陆需要的参数
        #_xsrf = response.xpath("//_xsrf").extract()[0]

        # 发送请求参数，并调用指定回调函数处理
        yield scrapy.FormRequest.from_response(
                response,
                formdata = {"username" : "18809236315", "password" : "995945908a"},#, "_xsrf" = _xsrf},
                callback = self.parse_page
            )

    # 获取登录成功状态，访问需要登录后才能访问的页面
    def parse_page(self, response):
        url = "https://www.lagou.com/zhaopin/Python/2/?filterOption=2"
        yield scrapy.Request(url, callback = self.parse_newpage)

    # 处理响应内容
    def parse_newpage(self, response):
        with open("xiao.html", "w") as filename:
            filename.write(response.body)