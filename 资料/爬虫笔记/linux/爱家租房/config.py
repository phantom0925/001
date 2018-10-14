# coding:utf-8

"""2.抽离配置文件"""

import os

#Application配置参数
settings = {
	"static_path":os.path.join(os.path.dirname(__file__),"static"),
	"template_path":os.path.join(os.path.dirname(__file__),"template"),	
	"cookie_secret":"eFWCId1LSrSdQkiKU+W9DhdeTo1AA0Sirl2sKK9lJzQ=",
	"xsrf_cookies":True,
	"debug":True
	}
# mysql
mysql_options = dict(
			host = "127.0.0.1",
			database = "ihome",
			user = "root",
			password = "mysql"
)
#redis
redis_options = dict(
			host = "127.0.0.1",
			port = 6379
)

#日志文件路径
log_file = os.path.join(os.path.dirname(__file__),"logs/log")
log_level = "debug"#日志等级