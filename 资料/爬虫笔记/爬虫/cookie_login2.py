# coding:utf-8

import urllib
import urllib2
import cookielib

#通过cookieJar()类创建一个cookieJar()对象，用来保存cookie值
cookie = cookielib.CookieJar()

#通过HTTPCookieProcessor()处理器构建一个处理器对象，用来处理cookie
#参数就是构建CookieJar()对象
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

#构建一个自定义的opener
opener = urllib2.build_opener(cookie_handler)

#自定义opener的addheaders的参数,可以赋值Http报头参数
opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36")]

#人人网的登陆接口
url = "http://www.renren.com/SysHome.do "
#模拟登陆就两步骤：先post你的账号密码，然后保存cookie用来下次登陆

#需要登陆的账户密码
data = {"email":"mr_mao_hacker@163.com","password":"alarmchime"}

#转换编码
data = urllib.urlencode(data)

#第一次post请求，发送需要登录的参数，获取cookie
request = urllib2.Request(url,data=data)

#发送第一次的post请求
response = opener.open(request)

#print response.read()

#第二次可以是get请求，这个请求将保存生成cookie一并发到web服务器，服务器会验证cookie通过
response_deng = opener.open("http://www.renren.com/410043129/profile")

#获取登录后才能访问的页面信息
print response_deng.read()

