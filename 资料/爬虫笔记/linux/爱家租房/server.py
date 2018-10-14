# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import config
import torndb
import redis

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from tornado.options import options,define
from tornado.web import RequestHandler
from urls import urls

define("port",default=8000,type=int,help="run server on the given port")

class Application(tornado.web.Application):
	""""""
	def __init__(self,*args,**kwargs):

		super(Application,self).__init__(*args,**kwargs)
		# self.db = torndb.Connection(
		# 	host = config.mysql_options["host"],
		# 	database = config.mysql_options["database"],
		# 	user = config.mysql_options["user"],
		# 	password = config.mysql_options["password"]
		# )
		self.db = torndb.Connection(**config.mysql_options)
		# self.redis = redis.StrictRedis(
		# 	host = config.redis_options["host"],
		# 	port = config.redis_options["port"]
		# 	)
		self.redis = torndb.StrictRedis(**config.redis_options)


def main():
	options.logging = config.log_level#日志等级
	options.log_file_prefix = config.log_file#日志文件路径
	tornado.options.parse_command_line()

	app = tornado.web.Application(urls,**config.settings)
	http_server = tornado.httpserver.HTTPServer(app)
	
	http_server.listen(options.port)

	tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
	main()