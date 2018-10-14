# coding:utf-8

from .BaseHandler import BaseHandler
import logging
from utils.captcha import captcha
import constants

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ImageCodeHandler(BaseHandler):
	""""""
	def get(self):
		code_id = self.get_argument("codeid")
		pre_code_id = self.get_argument("pcodeid")
		if pre_code_id:
			try:
				self.redis.delete("image_code_%s"%pre_code_id)
			except Exception as e:
				logging.error(e)
		#name图片验证码名称
		#text图片验证码文本
		#image图片验证码二进制数据		
		name,text,image = captcha.generate_captcha()

		try:
			#setex能同时设置键值以及中间的有效期时间
			self.redis.setex("image_code_%s"%code_id,constants.
				IMAGE_CODE_EXPIRES_SECONDS,text)
		except Exception as e:
			logging.error(e)
			self.write("")
		self.set_header("Content-Type","image/jpg")
		self.write(image)




