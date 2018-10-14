from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS()
driver.get("http://www.douban.com")

# 输入账号密码
driver.find_element_by_name("form_email").send_keys("xxxxx@xxxx.com")
driver.find_element_by_name("form_password").send_keys("xxxxxxxx")

# 模拟点击登录
driver.find_element_by_xpath("//div/input[@type='submit']").click()

# 等待3秒
time.sleep(3)

# 生成登陆后快照
driver.save_screenshot("douban.png")

with open("douban.html", "w") as file:
    file.write(driver.page_source)

driver.quit()

 driver.find_element_by_xpath('//form/div[@data-propertyname="username"]/input').send_keys("18809236315")
driver.find_element_by_xpath('//form/div[@data-propertyname="password"]/input').send_keys("995945908a")

#登陆
//div/input[@type='submit']

Cookie: JSESSIONID=ABAAABAAAGHAABH507ABFE06E128E8B095C5AF69ED958A7; _ga=GA1.2.148909248.1536626576; _gid=GA1.2.1527702521.1536626576; user_trace_token=20180911084412-cd14caa5-b55b-11e8-8e26-525400f775ce; LGSID=20180911084412-cd14d143-b55b-11e8-8e26-525400f775ce; LGUID=20180911084412-cd14d483-b55b-11e8-8e26-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536626576,1536626622; index_location_city=%E5%85%A8%E5%9B%BD; X_HTTP_TOKEN=c4442dbf902efffbfb78666b329a55f4; _ga=GA1.3.148909248.1536626576; TG-TRACK-CODE=undefined; ab_test_random_num=0; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536628638; LGRID=20180911091833-99f311b5-b560-11e8-8e2c-525400f775ce

isValidate=true&username=18809236315&password=06325907879e4c935552599c5d64d772&request_form_verifyCode=&submit=&challenge=3283f11a8b8225f86994668a6c62c3d7
