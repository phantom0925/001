# coding:utf-8

import os 
from handlers import VerifyCode
from handlers.BaseHandler import StaticFileBaseHandler as StaticFileHandler

urls = [
	(r"/api/piccode",VerifyCode.PicCodeHandler),
	(r"/(.*)",StaticFileHandler,
	dict(path=os.path.join(os.path.dirname(__file__),"html"),default_filename="index.html"))
]