# coding:utf-8

import Queue
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
		fullurl =  url + "&page" + str(page) + "&s" + str(s)
                print fullurl
		headers =  {}
		headers['User-Agent'] = random.choice(UAgent.u_agent)
		request = urllib2.Request(fullurl,headers=headers)
		respone = urllib2.urlopen(request).read()
		j_son(respone)

def j_son(respone):
	"""提取详情页"""
        print("---2---")
	html = etree.HTML(respone)
	html = html.xpath("//strong/a/@href")
	web_paths = Queue.Queue()
	for url in html:
		web_paths.put(url)
        vertical_crawl(web_paths)
def vertical_crawl(web_paths):
	"""详情页爬取"""
        print "---3---"
	web_path = "http:" + web_paths.get()
        print web_path
	# 从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
	dcap = dict(DesiredCapabilities.PHANTOMJS)
	dcap["phantomjs.page.settings.userAgent"] = (random.choice(UAgent.u_agent))  
	# 不载入图片，爬页面速度会快很多
	dcap[ " phantomjs.page.settings.loadImages " ] = False
	driver = webdriver.PhantomJS(desired_capabilities=dcap)
        print "---4---"
	driver.start_session(dcap)
        print "---5---"
	# 隐式等待5秒
	driver.implicitly_wait(5 )   
	# 设置1页面超时返回
        print "---6---"
	driver.set_page_load_timeout(20 )   
	# 设置1脚本超时时间
        print "---7---"
	driver.set_script_timeout(20)
        print "---8---"
	driver.maximize_window()
        print "---a0---"
        try:
	    driver.get(web_path)
            print "---a1---"
	    data = driver.page_source
	    soup = BeautifulSoup(data, 'lxml')
            print "---a2---"
	    #标题
	    title = soup.find('div',{'class':"sku-name"}).get_text().strip()
            print "title is:%s"%title
            print"---a3---"
            #价格
	    price = soup.find('span',{'class':"p-price"}).get_text()
            print "price is:%s"%price
	    #评论
    	    #comment = soup.find_all('s').get_text()
            print "---9---"
        except Exception as e:
            print "error is:%s"%e
            pass
#	json_dic = dict(
#		title = title,
#		price = price,
#		comment = comment
#		)

    	#write_page(json_dic)

#def write_page(json_dic):
#	"""写入爬取得内容"""
 #       print "---10---"
#	with open("./jdPhone.json","wb") as f:
#
#		f.write(json.dumps(json_dic))
#		print "加载完毕..."

if __name__ == "__main__":
        print "---0---"
	plane_page()





