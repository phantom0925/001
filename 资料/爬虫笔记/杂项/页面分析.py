#链接
links = response.xpath('//p[@class="title"]/a/@href').extract()

for link in links:

	url = "http://zu.fang.com"
	fullurl = url + link
	print fullurl

#标题
title = response.xpath('//h1[@class="title"]').extract()
#价格
price = response.xpath('//div[@class="trl-item sty1"]/i')
#单位+押金
unit = response.xpath('//div[@class="trl-item sty1"]/text()').extract()
#出租方式+朝向
rent_way_to = response.xpath('//div[@class="trl-item1 w146"]/div[@class="tt"]')
#户型+楼层
house_type_fl = response.xpath('//div[@class="trl-item1 w182"]/div[@class="tt"]')
#面积+装修
area_fit = response.xpath('//div[@class="trl-item1 w132"]/div[@class="tt"]')

#小区
little_area = response.xpath('//a[@id="agantzfxq_C02_07"]').extract()
#市区/:海淀区
city_area = response.xpath('//a[@id="agantzfxq_C02_08"]').extract()
#路：增光路
road = response.xpath('//a[@id="agantzfxq_C02_09"]').extract()
#地址
address = response.xpath('//div[@class="rcont"]/a').extract()

http://zu.fang.com/ 