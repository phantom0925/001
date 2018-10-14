# coding:utf-8

import urllib
import urllib2
import re

class Spider:
    def __init__(self):
        #初始化起始页的位置
        self.page = 2 
        #爬取开关
        self.switch = True

    def loadPage(self):
        """
        下载页面
        """
        url = "https://tieba.baidu.com/p/5532751792?pn=" + str(self.page)
        headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
        }
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
        #每页的html源码
        html = response.read()
        #print html
        #创建一个正则表达式规则对象，匹配每页里的段子内容，re.S表示匹配所有文本内容
        pattern = re.compile('<div\s(id)="([\w])"\sclass="d_post_content j_d_post_content">(.*?)</div>')
        
        #将正则匹配的对象引用到html源码字符串，返回这个页面里所有段子列表
        content_list = pattern.findall(html)
        #print content_list
        self.dealPage(content_list)
    def dealPage(self,content_list):
        """
            进一步处理页面中的特殊字符
        """
        for item in content_list:
            item = item.replace("<br>","")
            print item
            self.writePage(item)
    def writePage(self,item):
        """
            把每条段子逐个写入文件里
        """
        with open("duanzi.txt","a") as f:
            f.write(item)
    def startWork(self):
        """
            控制方法
        """

if __name__ == "__main__":
    duan_zi = Spider()
    duan_zi.loadPage()
