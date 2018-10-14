# coding:utf-8

from tornado.web import RequestHandler,StaticFileHandler


class BaseHandler(RequestHandler):
	"""自定义基类"""

	@property
	def db(self):
		"""作为RequestHandler对象的db属性"""

		return self.application.db
	@property
	def redis(self):
		"""作为RequestHandler对象的redis属性"""

		return self.application.redis

	def prepare(self):
		pass
	def set_default_headers(self):
		pass
	def on_finish(self):
		pass

class StaticFileBaseHandler(StaticFileHandler):
    """自定义静态文件处理类, 在用户获取html页面的时候设置_xsrf的cookie"""
    def __init__(self, *args, **kwargs):
        super(StaticFileBaseHandler, self).__init__(*args, **kwargs)
        self.xsrf_token