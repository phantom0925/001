# coding:utf-8

import urllib2

#代理开关，表示是否启用代理
proxyswitch = True

#构建一个Handler处理器对象，参数是一个字典类型，包括代理类型，代理服务器IP+PORT
httpproxy_handler = urllib2.ProxyHandler({"https":"114.113.126.87:80"})

#这是没有代理的写法
nullproxy_handler = urllib2.ProxyHandler({})

if proxyswitch:
    opener = urllib2.build_opener(httpproxy_handler)
else:
    opener = urllib2.build_opener(nullproxy_handler)

#构建了一个全局的opener,之后所有的请求都可以用urlopen()f方式发送，也附带handler的动能
urllib2.install_opener(opener)

request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)

print response.read()

