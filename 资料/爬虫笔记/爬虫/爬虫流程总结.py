1.cookie_login.py

"""
import urllib
import urllib2

headers:中多加一条cookie
url
#生成请求消息
request=urllib2.Request(url,data,headers)
#发送请求消息
response = urllib2.urlopen(request)
#读取请求消息
response.read()
"""
2.cookie_login2.py
"""
import urllib
import urllib2
import cookielib
#通过cookieJar创建一个cookieJardui对象，用来保存cookie
cookie = cookieilb.CookieJar()
#通过HTTPCookieProcessor()处理器构建一个处理器对象，用处就是处理cookie
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
#构建一个自定义的openor
opener = urllib2.build_opener(cookie_handler)
headers = {}
url 
data ={"账户":"","密码":""}
request = urllib2.Request(url,data,headers)
#发送第一次请求
response = opener.open(requeset)
#发送第二次请求可以使get请求，这个请求将保存到cookie一并发送到web服务器
response_two = opener.open("网址")
print response_two.read()
"""
3.https.py
"""
import urllib2
import ssl
#表示忽略ssl安全认证
context = ssl._create_unverified_context()
url 
headers
request = urllib2.Request(url,headers)
responser = urllib2.urlopen(request,context=context)
print response.read()
"""
4.tieba.py
"""
import urllib
import urllib2

def loadPage(fullurl,filename):
	headers = {...}
	request = urllib2.Request(...)
	return urllib2.urlopen().read()
def writePage(html,filename):
	with open(filename,"w") as f:
		f.write(html)
def  tiebaSpader(url,beginPage,endPage):
	for page in range(beginPage,endPage+1):
		pn = (page-1)*50#这是从页面中找出来的规律
		fullurl = url + "&pn=" + str(pn)
		html = loadPage(fullurl,filename)
		writePage(html,filename)
if __name__ == "__main__":
	fullurl = url+key 
	tiebaSpider(fullurl,beginPage,endPage)
"""
5.urllib2_ajax.py
"""
import urllib
import urllib2
url 
headers
data
data= urllib.unlencode(data)
request
response
"""
6.urllib2_proxyhandler.py
"""
import urllib2

httpproxyhandler = urllib2.ProxyHandler(xxx)
urllib2.install_opener(opener)
request
respose = urllib2.urlopen(request)
"""
7.处理器
"""
HTTPHandler =urllib2.HTTPHandler(debuglevel =1)
opener = urllib2.build_opener(HTTPHandler)

httpproxyhandler = urllib2.ProxyHandler({代理网址})
opener = urllib2.build_opener(httpproxyhandler)
urllib2.install_opener(opener)

cookie = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(cookie_handler)
opener = urllib2.build_opener(cookie_handler)
"""