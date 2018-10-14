
step1:创建项目

scrapy startproject xxx

step2：编写items.py文件
	
	设置需要保存的数据字段

step3:进入xxx/spiders
		
	编写爬虫文件，文件里name 就是爬虫名(不同于项目名)

step4:
	
	scrapy crawl itcast
	scrapy crawl itcast -o json/csv/xml


快速生成spider里的爬虫文件：scrapy genspider tencentPosition  "tencent.com"


INFO-->DEBUG-->WARING-->ERROR-->CRITICAL(错误等级排序)
