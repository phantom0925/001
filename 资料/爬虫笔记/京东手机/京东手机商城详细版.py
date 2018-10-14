# coding:utf-8

import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from lxml import etree
import json
import UAgent
import random
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def plane_page():
	"""索引页"""

	url = "http://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.1&vt=2&psort=3&cid2=653&cid3=655"
	page= -1
	s = -59
	while page<199:
		page += 2
		s += 60
		fullurl =  url + "&page" + str(page) + "&s" + str(s) + "&click=0"
		request = urllib2.Request(fullurl)
		headers =  {}
		headers['UAgent'] = random.choice(UAgent.u_agent)
		respone = urllib2.urlopen(request).read()
		j_son(respone)

def j_son(respone):
	"""提取详情页"""

	html = etree.HTML(respone)
	html = html.xpath("//strong/a/@href")

	for url in html:
		vertical_crawl(url)

def vertical_crawl(url):
	"""详情页爬取"""

	proxy_headers()
	driver.maximize_window()
	driver.get("//item.jd.com/5089253.html#comment")
	data = driver.page_source
	soup = BeautifulSoup(data, 'lxml')
	#标题
	title = soup.find('div',{'class':"sku-name"}).get_text().strip()
	#价格
	price = soup.find('span',{'class':"price J-p-7694047"}).get_text()
	#评论
	comment = soup.find('a',{'clstag':"shangpin|keycount|product|allpingjia_tuijianpaixu_NOTHING"}).get_text()

	json_dic = dict(
		title = title,
		price = price,
		comment = comment
		)
	with open("./jdPhone.json","wb") as f:

		f.write(json.dump(json_dic))
		print "加载完毕..."

def proxy_headers():
	"""设置请求头"""
	
	# proxy = Proxy(
	# {
	# "proxyType": ProxyType.MANUAL,
	# "httpProxy": "139.99.159.24:1001"
	# }
	# )
	# desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
	# 从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
	desired_capabilities[ " phantomjs.page.settings.userAgent " ] = (random.choice(UAgent.u_agent))   
	# 不载入图片，爬页面速度会快很多
	desired_capabilities[ " phantomjs.page.settings.loadImages " ] = False 
	# 把代理ip加入到技能中
	#proxy.add_to_capabilities(desired_capabilities)
	# PhantomJS 
	driver = webdriver.PhantomJS()
	driver.start_session(desired_capabilities)   
	# 隐式等待5秒，可以自己调节
	driver.implicitly_wait(5 )   
	# 设置10秒页面超时返回，类似于requests.get()的timeout选项，driver.get()没有timeout选项 
	# 以前遇到过driver.get(url)一直不返回，但也不报错的问题，这时进程会卡住，设置超时选项能解决这个问题。
	driver.set_page_load_timeout(20 )   
	# 设置10秒脚本超时时间
	driver.set_script_timeout(20) 
	return driver

if __name__ == "__main__":

	plane_page()
