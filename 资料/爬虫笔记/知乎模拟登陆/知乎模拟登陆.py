#coding:utf-8

import requests
import time
import random
from UAgent import u_agent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains


def zhihu_login():
	"""登陆"""
        desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
        #随机设置一个浏览器头
        desired_capabilities["phantomjs.page.settings.userAgent " ] = (random.choice(u_agent))
        driver = webdriver.PhantomJS()
        driver.get("https://www.zhihu.com/signin?next=%2F")
        driver.start_session(desired_capabilities)
        #隐式等待秒，可以自己调节
        driver.implicitly_wait(10) 
        driver.maximize_window()
        
        driver.get("https://www.zhihu.com/signup")
         #定位到登录按钮，切换到输入用户名和密码模式
        driver.find_element_by_css_selector('.SignContainer-switch span').click()
		#输入用户名和密码
        driver.find_element_by_css_selector('input[name="username"]').send_keys('18809236315')
        driver.find_element_by_css_selector('input[name="password"]').send_keys('995945908')
        driver.save_screenshot("zhihu.png")	
        #请输入验证码
        if_captcha = raw_input("是否输入验证:(y/n):")
        if if_captcha == 'y':
            captcha = raw_input("请输入验证码:")
            driver.find_element_by_name("captcha").send_keys(captcha)
            driver.save_screenshot("zh.png")	
            login(driver)
        elif if_captcha == 'n':
            login(driver)
def login(driver):
        # 模拟点击登录
        driver.find_element_by_xpath("//button[@type='submit']").click()
        #ActionChains(driver).double_click(box).perform()
        time.sleep(10)
        #driver.implicitly_wait(30) 
        driver.save_screenshot("zhihu2.png")
        clicks = raw_input("请输入指令继续爬取(y/n):")

        if clicks == 'y':
            #请输入验证码
            if_captcha = raw_input("是否输入验证:(y/n):")
            if if_captcha == 'y':
                captcha = raw_input("请输入验证码:")
                driver.find_element_by_name("captcha").send_keys(captcha)
                driver.find_element_by_xpath("//button[@type='submit']").click()
            elif if_captcha == 'n':
                driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.save_screenshot("zhihu3.png")
        cookies = driver.get_cookies()
        print cookies
        is_login(cookies)

def is_login(cookies):
	"""判断是否登录成功"""

	header = {
	    "HOST":"www.zhihu.com",
	    'User-Agent': random.choice(u_agent),
	    'cookies':cookies[0]
	}
        get_index(header)    
	inbox_url = "https://www.zhihu.com/people/wang-shuai-shuai-28/activities"
	response = requests.get(inbox_url,headers=header,allow_redirects=False)
	if response.status_code != 200:
		return False
	else:
                print response
		return True

def get_index(header):
	"""在登陆过的情况下使用这个方法"""
	response = requests.get("https://www.zhihu.com/people/wang-shuai-shuai-28/activities",headers=header)
	with open("index_page.html","wb") as f:
		f.write(response.text.encode("utf-8"))
                print "ok"

if __name__ == "__main__":
	zhihu_login()
