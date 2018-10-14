# coding:utf-8

import urllib
import urllib2

def loadPage(fullurl,filename):
    """
    作用：根据url发送请求，获取服务器响应文件
    url:需要爬取的url地址
    filename：处理的文件名
    """
    print "正在下载" + filename
    headers = {"Host":"tieba.baidu.com",
            "Connection":"keep-alive",
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "X-Requested-With":"XMLHttpRequest",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/  67.0.3396.87 Safari/537.36",
            "Accept-Language":"zh-CN,zh;q=0.9",}

    request = urllib2.Request(fullurl,headers=headers)
    
    return urllib2.urlopen(request).read()


def writePage(html,filename):
    """
    作用：将html内容写入到本地
    html：服务器响应文件内容
    """
    print "正在保存" + filename
    with open(filename,"w") as f:
        f.write(html)
    print "*"*30

def tiebaSpider(url,beginPage,endPage):
    """
    作用：贴吧爬虫调度器负责组合处理每个页面的url
    url:贴吧url的前部分
    begin Page：起始页码
    endPage:终止页
    """
    for page in range(beginPage,endPage+1):
        tpl = (page-1)*50
        filename = "第" + str(page) + "页.html"
        fullurl = url + "&tpl=" + str(tpl)
        #print fullurl
        html = loadPage(fullurl,filename)
        #print html
        writePage(html,filename)
    print "thanks for using"


if __name__ == "__main__":

    kw = raw_input("请输入贴吧名:")
    beginPage = int(raw_input("请输入起始页码:"))
    endPage = int(raw_input("请输入结束页码:"))
    url = "https://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw":kw})#接收的是字典
    fullurl = url + key

    tiebaSpider(fullurl,beginPage,endPage)
