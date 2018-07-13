#!/usr/bin/env python3
# -*- coding : utf-8 -*-

"""
方便管理博客上传的图片样式，编写这个图片工具程序
"""

import operator as op
from enum import Enum, unique
import os
import os.path
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
		if name.find('.') != -1:
			name = name[:name.index('.')]
			print(name)
		# 打开文件
		img = Image.open(file)
		# 重置大小
		new_img = img.resize((w, h), resample=Image.ANTIALIAS)
		# 判断保存路径是否为空，为空就保存到原始目录下
		if not nf.strip():
			nf = file[:file.rindex('/')]
		# 保存新的图片文件
		new_img.save(nf + '/' + name + '_' + str(w) + '_' + str(h) + self.get_type(self, t=t), t.value)
		return True
	
	# 批量处理
	def img_dir(self, d, w=600, h=400, nf='', t=ImgType.PNG):
		# 转换字符
		dir = d.replace('\\', '/')
		# 遍历目录，得到父目录，子文件夹，文件
		for parent, dirns, fns in os.walk(d):
			# 遍历文件
			for file in fns:
				# 判断是否文件
				if os.path.isfile(dir + '/' + file):
					# 剔除 .ini 格式文件
					if '.ini' not in file:
						self.img_cop(self, d + '/' + file, w=w, h=h, nf=nf, t=t)
		pass
	
	# 根据类型获取后缀名
	@staticmethod
	def get_type(self, t):
		# 比较字符串是否相同
		if op.eq(t.value, ImgType.JPG.value):
			return '.jpg'
		elif op.eq(t.value, ImgType.PNG.value):
			return '.png'
