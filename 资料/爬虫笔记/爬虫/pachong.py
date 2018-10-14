#coding:utf-8

import urllib.request, urllib.error, urllib.parse  #===>由urllib2转换而来
import json
import jsonpath


url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"}

request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)

#去除json文件里的字符串内容
html = response.read()

#把json形式的字符串转化成python形式的unicode字符串
unicodestr = json.loads(html)#json.load改为了loads

#python形式的列表
city_str_list = jsonpath.jsonpath(unicodestr,"$..")

for item in city_str_list:
	print(item)
#返回的unicode字符串
array = json.dumps(city_str_list,ensure_ascii=False)
with open("lagoucity.json","wb") as f:
	f.write(array.encode("utf-8"))