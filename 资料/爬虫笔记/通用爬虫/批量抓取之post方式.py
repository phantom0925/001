yu# coding:utf-8
import urllib
import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding("utf8")
# POST请求的目标URL
url = "https://m.fang.com/zf/bj/AGT_415595884.html"

headers={
	"Accept": "application/json, text/javascript, */*; q=0.01",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"Cookie": "integratecover=1; SoufunSessionID_Rent=1_1537098148_1253; global_cookie=mr2oliibx27d5q8e2plafymsj5cjm4shx3d; polling_imei=a402c2c7e22f1ac8; ASP.NET_SessionId=ifpgjc30jqzkfvlgfdyladpn; sf_source=; s=; showAdbj=1; Rent_StatLog=115d3a22-ad26-48f9-9dcd-eab82c30425f; indexAdvLunbo=lb_ad1%2C0%7Clb_ad2%2C0%7Clb_ad3%2C0%7Clb_ad4%2C0%7Clb_ad6%2C0; city=www; unique_cookie=U_omuet3bl3pik5h9ycn5q6vqm124jm8urph6*26; Captcha=676D6D64694A372F326C4B70737142635A4A725954644F704674325742636A3858796456584938697558366D334E554D3539594B4272303261394C36715377516251714D565A59387273553D"
}

# formdata = {
# 	"projcode":"1010234143",
# 	"houseid":"414480552",
# 	"detailType":"jjr",
# 	"rentType":"zz",
# 	"purpose":"%25u4F4F%25u5B85",
# 	"room":"3",
# 	"num":"3"
# }

#data = urllib.urlencode(formdata)

#request = urllib2.Request(url, data = data, headers = headers)
request = urllib2.Request(url, headers = headers)
response = urllib2.urlopen(request).read()
if isinstance(response, unicode):
    response=response.encode('utf-8')
else:
    response=response.decode('gbk','ignore').encode('utf-8')
print response
# js_dict = json.loads(response)
# for i in js_dict:
# 	print i

