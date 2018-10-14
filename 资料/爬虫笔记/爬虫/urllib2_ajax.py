# coding:utf-8

import urllib
import urllib2

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="

headers ={
       
        "Host":"movie.douban.com", 
        "Connection":"keep-alive", 
        "X-Requested-With":"XMLHttpRequest", 
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36" 
        }
startPage = input("请输入开始页码:")
endPage = input("请输入终止页码:")
formdata = {
        "start":startPage,
        "limit":endPage
        }

data = urllib.urlencode(formdata)
request = urllib2.Request(url,data=data,headers=headers)
t = urllib2.urlopen(request).read()
with open("movie.json","w") as f:
    f.write(t)


