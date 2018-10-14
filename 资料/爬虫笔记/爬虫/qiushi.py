# coding:utf-8

import urllib
import urllib2
import json
from lxml import etree

bpage = int(raw_input("请输入要爬取的开始页码:"))
epage = int(raw_input("请输入要爬取得结束页码:"))
for i in range(bpage,epage+1):
    url = "https://www.qiushibaike.com/8hr/page/"+str(i)
headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
        }
request = urllib2.Request(url,headers=headers)
html = urllib2.urlopen(request).read()

#响应返回的是字符串，解析后为html—Dom模式
text = etree.HTML(html)

#创建一个根节点,返回的是所有段子的节点位置，contain()模糊查询方法，第一个参数返回的是匹配的标签，第二个参数返回的是标签名的部分内容
node_list = text.xpath('//div[contains(@id,"qiushi_tag")]')
items = {}
#遍历根节点，
for node in node_list:
    #用户名
    username= node.xpath('./div/a/@title')[0]
    #内容.text表取里面的内容,xpath返回的是一个列表用索引方式取出来，其实就返回一个列表所以索引[0]
    content = node.xpath('.//div[@class="content"]/span')[0].text
    #点赞
    dianzan = node.xpath('.//i')[0].text
    #评论
    comments = node.xpath('.//i')[1].text
    #图片链接
    imageLink = node.xpath('./div[@class="thumb"]/a/img/@src')

    items = {
            "username":user,
            "content":content,
            "comments":comments,
            "dianzan":dianzan,
            "imageLink":imageLink
                                }
    with open("qiushi.json","a") as f:
        f.write(json.dumps(items,ensure_ascii=False).encode("utf-8")+"\n")

