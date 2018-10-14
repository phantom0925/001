# coding:utf8

import urllib
import urllib2

#通过抓包的方式获取url
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

#完整的headers
headers = {
        "Host":"fanyi.youdao.com", 
        "Content-Length":"221", 
        "Accept":"application/json, text/javascript, */*; q=0.01", 
        "X-Requested-With":"XMLHttpRequest", 
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36", 
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8", 
        "Accept-Language":"zh-CN,zh;q=0.9", } 
key = raw_input("请输入要翻译的内容:")

#发送到web服务器的表单数据
formdata = {
        "i":key, 
        "from":"en", 
        "to":"zh-CHS", 
        "smartresult":"dict", 
        "client":"fanyideskweb", 
        "salt":"1535719973083", 
        "sign":"44ebdd3918f2f0b6ea16afa5862071bf", 
        "doctype":"json", 
        "version":"2.1", 
        "keyfrom":"fanyi.web", 
        "action":"lan-select", 
        "typoResult":"false", 
        }
#经过urlencode转码
data = urllib.urlencode(formdata)

#如果Request方法的data参数有值，那么这个请求就是post
#如果没有就是get
request = urllib2.Request(url,data=data,headers=headers)

print urllib2.urlopen(request).read()

