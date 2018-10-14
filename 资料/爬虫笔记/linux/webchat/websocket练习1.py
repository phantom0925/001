# coding:utf-8
import tornado.options
from tornado.options import define
from tornado.web import  Application,RequestHandler
from tornado.websocket import WebSocketHandler
import torndb
import os
import tornado.httpserver
import tornado.ioloop

define("port",default=8000,type=int,help="runing")

class IndexHandler(RequestHandler):
	"""首页"""
        def get(self):
            self.render("websocket练习1.html")


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


class Application(Application):

	def __init__(self,*args,**kwargs):

		super(Application,self).__init__(*args,**kwargs)

		self.db = torndb.Connection(
			host = "127.0.0.1",
			database = "itcast",
			user = "root",
			password = "mysql"
			)

if __name__ == "__main__":

	tornado.options.parse_command_line()
	settings = dict(
		static_path = os.path.join(os.path.dirname(__file__),"static"),
		template_path = os.path.join(os.path.dirname(__file__),"template"),
		debug = True,
		cookie_secret = "",
		xsrf_cookies = True,
		login_url = "/login"
		)
	app = Application([
		(r"/",IndexHandler),
		(r"/chat",ChatHandler),
		],**settings)

	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(tornado.options.options.port)

	tornado.ioloop.IOLoop.current().start()

