#coding:utf-8

import urllib2

#authproxy_handler = urllib2.ProxyHandler({"http":"mr_mao_hacker:ssfqry9r&114.215.104.49:16816"})
#通常账号密码不是直接写在文件里的，可以写在一个模块里导入
#也可以放在系统变量里：
    """
    比如用户目录下面有 vi ~/.bash_profile
    在文件最上面加入系统环境变量：
        proxyuser = mr_mao_hacker
        proxypasswd = ssfqry9r
        export proxyuser
        export passwd
    对文件生效：$:source ~/.bash_profile
    建好了怎么在程序里去呢？
        import os#sys是和python系统相关的，os是操作系统相关的

        name =os.environ.get("proxyuser")
        print name 
    然后执行就可以取到了：python xxx.py
"""
proxyuser = os.environ.get("proxyuser")
passwd = os.environ.get("passwd")

authproxy_handler = urllib2.ProxyHandler({"http":proxyuser+":"+passwd+"@114.215.104.49:16816"})
#构建一个自定义的opener
opener = urllib2.build_opener(authproxy_handler)
#构建请求
request = urllib2.Request("http://www.baidu.com/")
#获取响应
response = opener.open(request)
#返回响应内容
print response.read()
