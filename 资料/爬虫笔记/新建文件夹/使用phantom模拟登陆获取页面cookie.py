#使用PhantomJS模拟登录，获取页面cookie
from selenium import webdriver
from time import sleep
class Cookie:
    def cookie_add(self,name,pwd):
        self.driver=webdriver.PhantomJS()
        self.driver.get('https://id.oppo.com/login ')  #此处url填写需要访问的地址
        self.driver.find_element_by_id('identity').send_keys(name)
        self.driver.find_element_by_id('password').send_keys(pwd)
        self.driver.find_element_by_id('loginBtn').click()
        sleep(3)
        self.driver.get('https://www.oppo.cn')
        self.cookie_list =self.driver.get_cookies()
        self.cookie_dict = {}
        for cookie in self.cookie_list:
            self.cookie_dict[cookie['name']] = cookie['value']
        sun=[]
        for key in self.cookie_dict:  #讲字典转换为字典
            sun.append(key+'='+self.cookie_dict[key]+';')
        cookies=''.join(list(sun))[:-1]
        return cookies

#使用urllib库，发送接口请求
import urllib.parse,urllib.request
class Urlopen:

    def __init__(self,url,data={},header=''):
        self.url=url
        self.data= urllib.parse.urlencode(data).encode('utf-8')
        self.header=header

    def open(self):
        req=urllib.request.Request(self.url,self.data)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0')
        req.add_header('Cookie',self.header)
        res=urllib.request.urlopen(req)
        html=res.read().decode('utf-8')
        return html


#使用cookie完成点赞操作
from LoginCookie import Requ,login_cookie
def Like():
    url='https://www.oppo.cn/thread/praise/create.json'
    data={'tid':'163840351','author_uid':'77141646','type':'0'}
    cookie=login_cookie.Cookie().cookie_add('账号','密码')
    html=Requ.Urlopen(url=url,data=data,header=cookie).open()
    print(html)
Like()