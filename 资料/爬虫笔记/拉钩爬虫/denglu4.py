#!/usr/bin/env python
# -*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy import Request, FormRequest
from zhihu.items import ZhihuItem

class Denglu4Sipder(CrawlSpider) :
    name = "denglu4"
    allowed_domains = ["www.lagou.com"]
    start_urls = [
        "http://www.lagou.com"
    ]

    rules = (
        Rule(LinkExtractor(allow = ('/zhaopin/Python/?labelWords', )), callback = 'parse_page', follow = True),
        Rule(LinkExtractor(allow = ('/jobs/\d+.html')), callback = 'parse_page', follow = True),
    )

    headers = {
    "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
    "Referer: https":"//www.lagou.com/jobs/4254613.html",
    "Cookie":" WEBTJ-ID=20180911084251-165c614c3d8186-0bb03045493bb9-5701631-1044480-165c614c3da16e; _ga=GA1.2.148909248.1536626576; _gid=GA1.2.1527702521.1536626576; user_trace_token=20180911084412-cd14caa5-b55b-11e8-8e26-525400f775ce; LGSID=20180911084412-cd14d143-b55b-11e8-8e26-525400f775ce; LGUID=20180911084412-cd14d483-b55b-11e8-8e26-525400f775ce; JSESSIONID=ABAAABAAAGFABEF4EEE9871F6F89CFA9D4E3550FFE2AEB9; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536626576,1536626622; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_navigation; X_HTTP_TOKEN=c4442dbf902efffbfb78666b329a55f4; ab_test_random_num=0; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; LG_LOGIN_USER_ID=599045487377ba5df19afeea197eb4adb5a70532b3a6649ae680c93a0dc078ab; _putrc=D49C284382A8B020123F89F2B170EADC; login=true; unick=%E7%8E%8B%E5%B9%BF%E6%96%87; gate_login_token=d757c111b329f0a9e439451b4c0b8d36d553cf9273d6b3ce662a16c609fc1ab2; SEARCH_ID=082c1b27ccd74baf9f2e917f007a689e; _gat=1; LGRID=20180911105854-9e7965a8-b56e-11e8-b68b-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536634659"
    }

    #重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    def start_requests(self):
        return [Request("https://passport.lagou.com/login/login.html", meta = {'cookiejar' : 1}, callback = self.post_login)]

    def post_login(self, response):
        print 'Preparing login'
        #下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
        # xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
        # print xsrf
        #FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
        #登陆成功后, 会调用after_login回调函数
        return [FormRequest.from_response(response,   #"http://www.zhihu.com/login",
                            meta = {'cookiejar' : response.meta['cookiejar']},
                            headers = self.headers,  #注意此处的headers
                            formdata = {
                            # '_xsrf': xsrf,
                            'username': '18809236315',
                            'password': '995945908a'
                            },
                            callback = self.after_login,
                            dont_filter = True
                            )]

    def after_login(self, response) :
        for url in self.start_urls :
            yield self.make_requests_from_url(url)

    def parse_page(self, response):
        problem = Selector(response)
        print response.url
        # item = ZhihuItem()
        # item['url'] = response.url
        # item['name'] = problem.xpath('//span[@class="name"]/text()').extract()
        # print item['name']
        # item['title'] = problem.xpath('//h2[@class="zm-item-title zm-editable-content"]/text()').extract()
        # item['description'] = problem.xpath('//div[@class="zm-editable-content"]/text()').extract()
        # item['answer']= problem.xpath('//div[@class=" zm-editable-content clearfix"]/text()').extract()
        # return item