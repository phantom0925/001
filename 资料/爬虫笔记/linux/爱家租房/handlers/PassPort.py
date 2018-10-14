# coding:utf-8

from .BaseHandler import BaseHandler
import logging#开启日志功能

class IndexHandler(BaseHandler):

	def get(self):
		logging.debug("debug msg")
		logging.info("info msg")#正常信息
		logging.warning("warning msg")#有些错误		
		logging.error("error msg")#严重错误
		print "print msg"
		self.write("hello itcast")
