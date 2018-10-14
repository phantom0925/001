# coding:utf-8

import urllib2
import ssl

#表示我忽略ssl安全认证
context = ssl._create_unverified_context()
url = "https:///www.12306.cn/mormhweb/"
headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
        }
request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request,context=context)

print response.read()
