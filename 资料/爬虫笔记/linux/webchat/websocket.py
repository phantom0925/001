# coding:utf-8
# webSocket是HTML5规范中新提出的客户端-服务器通讯协议，协议本身使用新的ws://URL格式
# 是独立的创建在TCP协议之上的,和http的唯一关联是使用HTTP协议的101状态码进行协议切换，使用的TCP端口是80，可以用于绕过大多数防火墙的限制
# 允许服务端直接向客户端发送数据而不需要客户端进行请求，两者之间创建持久型的链接，并允许数据进行双向传递。

from tornado.websocket import WebSocketHandler
from tornado.web import RequestHandler
from tornado.options import options,define

import tornado.options
import tornado.web
import tornado.httpserver
import tornado.ioloop
import os
import torndb


tornado.options.define("port",default=8000,type=int,help="server running")

class IndexHandler(RequestHandler):

	def get(self):
		self.render("webchat.html")

class ChatHandler(WebSocketHandler):

	users = []

	def open(self):
		
		for user in self.users:
			user.write_message(u"%s上线了"%self.request.remote_ip)
		self.users.append(self)

	def on_message(self,msg):

		for user in self.users:
			user.write_message(u"%s说:%s"%(self.request.remote_ip,msg))

	def on_close(self):

		self.users.remove(self)
		for user in self.users:
			user.write_message(u"%s下线了"%self.request.remote_ip)

	def check_origin(self,origin):

		return True

class Application(tornado.web.Application):

	def __init__(self,*args,**kwargs):

		super(Application,self).__init__(*args,**kwargs)
		#数据库接口
		self.db = torndb.Connection(
			host = "127.0.0.1",
			database = "itcast",
			user = "root",
			password = "mysql"
			)

if __name__ == "__main__":

	tornado.options.parse_command_line()

	current_path = os.path.dirname(__file__)
	
	settings = dict(
		static_path = os.path.join(current_path,"static"),
		template_path = os.path.join(current_path,"template"),
		debug = True,
		cookie_secret = "2hcicVu+TqShDpfsjMWQLZ0Mkq5NPEWSk9fi0zsSt3A=",
	)

	app = Application([
		(r"/",IndexHandler),
		(r"/chat",ChatHandler),
		],**settings)

	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(tornado.options.options.port)

	tornado.ioloop.IOLoop.current().start()


