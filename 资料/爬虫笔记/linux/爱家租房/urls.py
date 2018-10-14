# coding:utf-8

"""1.抽离路由"""
import os
from handlers import PassPort,VerifyCode
from tornado.web import StaticFileHandler

urls = [
	(r"/",PassPort.IndexHandler),
	(r"/api/imagecode",VerifyCode.ImageCodeHandler),
	(r"/(.*)",StaticFileHandler,dict(path=os.path.join(os.path.dirname(__file__),"html"),default_filename="index.html"))
]