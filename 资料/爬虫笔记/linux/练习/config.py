# coding:utf-8

import os 

current_path = os.path.dirname(__file__)

#Application配置参数
settings = dict(
	static_path = os.path.join(current_path,"static"),
	cookie_secret = "FhLXI+BRRomtuaG47hoXEg3JCdi0BUi8vrpWmoxaoyI=",
	xsrf_cookies = True,
	debug = True
	)
#数据库参数配置
mysql_options = dict(
	host = "127.0.0.1",
	database = "ihome",
	user = "root",
	password = "mysql"
	)
#redis参数配置
redis_options = dict(
	host = "127.0.0.1",
	port = 6379
	)

#日志配置
log_path = os.path.join(current_path,"logs/log")
log_level = "debug"
