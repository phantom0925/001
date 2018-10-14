"""
获取AJAX加载的内容
有些网页内容使用AJAX加载，只要记得，AJAX一般返回的是JSON,直接对AJAX地址进行post或get，就返回JSON数据了。
"作为一名爬虫工程师，你最需要关注的，是数据的来源"
"""
"""
为什么有时候POST也能在URL内看到数据？
GET方式是直接以链接形式访问，链接中包含了所有的参数，服务器端用Request.QueryString获取变量的值。
如果包含了密码的话是一种不安全的选择，不过你可以直观地看到自己提交了什么内容。

POST则不会在网址上显示所有的参数，服务器端用Request.Form获取提交的数据，
在Form提交的时候。但是HTML代码里如果不指定 method 属性，则默认为GET请求，Form中提交的数据将会附加在url之后，以?分开与url分开。

表单数据可以作为 URL 字段（method="get"）或者 HTTP POST （method="post"）
的方式来发送。比如在下面的HTML代码中，表单数据将因为 （method="get"） 而附加到 URL 上：
"""
import urllib
import urllib2

# demo1

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

headers={"User-Agent": "Mozilla...."}

# 变动的是这两个参数，从start开始往后显示limit个
formdata = {
    'start':'0',
    'limit':'10'
}
data = urllib.urlencode(formdata)

request = urllib2.Request(url, data = data, headers = headers)
response = urllib2.urlopen(request)

print response.read()


# demo2

url = "https://movie.douban.com/j/chart/top_list?"
headers={"User-Agent": "Mozilla...."}

# 处理所有参数
formdata = {
    'type':'11',
    'interval_id':'100:90',
    'action':'',
    'start':'0',
    'limit':'10'
}
data = urllib.urlencode(formdata)

request = urllib2.Request(url, data = data, headers = headers)
response = urllib2.urlopen(request)

print response.read()