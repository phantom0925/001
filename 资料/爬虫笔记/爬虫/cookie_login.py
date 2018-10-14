# coding:utf-8

import urllib
import urllib2

headers ={
        "Host":" weibo.com", 
        "Cache-Control":" max-age=0", 
        "Upgrade-Insecure-Requests":" 1", 
        "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36", 
        "Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
        "Accept-Language":" zh-CN,zh;q=0.9", 
        "Cookie": "SINAGLOBAL=1206240902212.2366.1534155160516; YF-Ugrow-G0=8751d9166f7676afdce9885c6d31cd61; SUB=_2AkMs1Xaxf8NxqwJRmP4Qzm7gbo12yA_EieKaiYdqJRMxHRl-yT83qkcmtRB6B1VYXjT6Atg7KTlshpyP7ZvvIQ7dUtGo; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5jyROpbXeOrGgW8u63iZ6e; login_sid_t=7b8f0cccab706ba3372ee7905d4bc8c8; cross_origin_proto=SSL; YF-V5-G0=b1e3c8e8ad37eca95b65a6759b3fc219; wb_view_log=1360*7681; _s_tentry=passport.weibo.com; Apache=2666527280592.534.1535768921156; ULV=1535768921187:4:1:3:2666527280592.534.1535768921156:1535702164214; UOR=,,graph.qq.com; YF-Page-G0=f994131fbcce91e683b080a4ad83c421"
        }

a = int(input("1或2"))
if a == 1:
    x = "1005055014_"
    y = "1"
elif a == 2:
    x = "1005055014_"
    y = "1"
else:
    x = input("请输入refer_flag:")
    y = input("请输入is_hot:")
url = "https://weibo.com/u/1537790411?refer_flag=%s&is_hot=%s"%(x,y)
request = urllib2.Request(url,headers=headers)
print request
response = urllib2.urlopen(request)

print response.read()
