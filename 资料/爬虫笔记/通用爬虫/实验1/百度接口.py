import urllib
import urllib2
import random
from collections import deque
from lxml import etree

url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&"
wd = raw_input("请输入你要查询的内容：")
key = urllib.urlencode({"wd" : wd})
fullurl = url + key

u_list = [
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60' 
	'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50' 
	'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50' 
	'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)'
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'
	'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5' 
	'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'
	'Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1' 
	'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
]

user_agent = random.choice(u_list)

request = urllib2.Request(fullurl)
#添加一个headers
request.add_header("User-Agent", user_agent)

#返回搜索页
html = urllib2.urlopen(request).read()

#获得第一层链接
html = etree.HTML(html)
oneheaderLinks = html.xpath('//div[@class="op_exactqa_body"]//div/p[@class="op_exactqa_item_img"]/a/@href')

for oneheaderLink in oneheaderLinks:

	oneLink = "http://www.baidu.com" + oneheaderLink

	request = urllib2.Request(oneLink)

	request.add_header("User-Agent", user_agent)

	#返回搜索页
	html = urllib2.urlopen(request).read()

	#获得第一层链接
	html = etree.HTML(html)
	twoheaderLink = html.xpath('//div[@class="op_exactqa_body"]//div/p[@class="op_exactqa_item_img"]/a/@href')[0]

	print twoheaderLink

	











