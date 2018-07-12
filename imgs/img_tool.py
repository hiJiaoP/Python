#!/usr/bin/env python3
# -*- coding : utf-8 -*-

"""
方便管理博客上传的图片样式，编写这个图片工具程序
"""

import operator as op
from enum import Enum, unique

from PIL import Image


# 图片类型
# 枚举类型，调用需要 .value或者 .name
@unique
class ImgType(Enum):
	JPG = 'jpeg'
	PNG = 'png'


# 工具程序
class ImgTool:
	
	def __init__(self):
		pass
	
	# 压缩单张图片至指定宽高
	def img_cop(self, f, w=600, h=400, nf='', t=ImgType.PNG):
		# 将路径中的 \ 转换为 /
		file = f.replace('\\', '/')
		# 获取文件名字
		name = file[file.rindex('/') + 1:]
		# 打开文件
		img = Image.open(file)
		# 重置大小
		new_img = img.resize((w, h), resample=Image.ANTIALIAS)
		if not nf.strip():
			nf = file[:file.rindex('/')]
			print(nf)
		# 保存新的图片文件
		new_img.save(nf + '/new_' + name + self.get_type(self, t=t), t.value)
		return True
	
	# 根据类型获取后缀名
	@staticmethod
	def get_type(self, t):
		# 比较字符串是否相同
		if op.eq(t.value, ImgType.JPG.value):
			return '.jpg'
		elif op.eq(t.value, ImgType.PNG.value):
			return '.png'
