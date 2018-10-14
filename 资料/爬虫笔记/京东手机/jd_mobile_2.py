# coding:utf-8

import sys
import re
import Queue
import urllib2
from lxml import etree
import json
import UAgent
import random
import requests

reload(sys)
sys.setdefaultencoding("utf-8")

def plane_page():
    """索引页"""

    url = "http://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.1&vt=2&psort=3&cid2=653&cid3=655"
    page= -1
    s = -59
    while page<199:
        page += 2
        s += 60
        fullurl =  url + "&page" + str(page) + "&s" + str(s)
        headers =  {}
        headers['User-Agent'] = random.choice(UAgent.u_agent)
        request = urllib2.Request(fullurl,headers=headers)
        respone = urllib2.urlopen(request).read()
        next_link(respone)

def next_link(respone):
    """提取详情页链接"""
    html = etree.HTML(respone)
    html = html.xpath("//strong/a/@href")
    #创建Queue对象用来存储详情页的链接
    web_paths = Queue.Queue()
    for url in html:
            url = url.split('#')[0]
            web_paths.put(url)
    vertical_crawl(web_paths)

def vertical_crawl(web_paths):
    """详情页爬取"""    
    while not web_paths.empty():
        web_path = "http:" + web_paths.get()
        print "-----详情页开始加载====>"
        print web_path
        headers = {}
        headers['User-Agent'] = random.choice(UAgent.u_agent)
        request = urllib2.Request(web_path,headers=headers)
        html  = urllib2.urlopen(request).read()
        html = etree.HTML(html)
        #获取标题
        title = html.xpath(".//div[@class='sku-name']/text()")[0].strip()
        if len(title) != 0:
            js_dict_parse(web_path,title)
        else:
            print "===空的====>"
            title = html.xpath(".//div[@class='sku-name']/text()")[1].strip()
            print title
            js_dict_parse(web_path,title)
        
def js_dict_parse(web_path,title):
    """解析json数据"""
    #提取id
    id = re.findall(r"\d+",web_path)[0]
    print id
    print title
    headers = {}
    headers['User-Agent'] = random.choice(UAgent.u_agent)
    #产品价格json网址
    price_link = "https://p.3.cn/prices/mgets?skuIds=J_" + str(id)
    response = requests.get(price_link)
    js = response.text
    js = json.loads(js)

    for item in js:
        price = item["p"]
        print price 

    #评论json网址
    comment_link = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds=" + str(id)
    response = requests.get(comment_link)
    js = response.text
    js = json.loads(js)
    for item in js["CommentsCount"]:
        #总评
        CommentCount = item["CommentCount"]
        #好评
        GoodCount = item['GoodCount']
        #中评
        GeneralCount = item['GeneralCount']
        #差评
        PoorCount = item['PoorCount']
    write_page(title,price,CommentCount,GeneralCount,GoodCount,PoorCount)

def write_page(title,price,CommentCount,GeneralCount,GoodCount,PoorCount):
    """写入数据"""
    d_dict = dict(
        title = title,
        price = price,
        CommentCount = CommentCount,
        GoodCount = GoodCount,
        PoorCount = PoorCount,
        )
    print d_dict
    print "=====开始写入===>"
    with open("./product_info.csv","a") as f:
        f.write(json.dumps(d_dict).decode("unicode-escape"))
        print "---写入完毕----"
if __name__ == "__main__":

    plane_page()





