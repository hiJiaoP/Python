#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import wx
from imgs.img_tool import *


class ImgToolUI(wx.Frame):
	# 单张图片输入框
	tc_file = None
	# 面板
	p = None
	# 文件夹输入框
	tc_dir = None
	# 宽输入框
	tc_width = None
	# 高输入框
	tc_height = None
	# 保存路径输入框
	tc_save = None
	
	def __init__(self, title='Img Tools'):
		super(ImgToolUI, self).__init__(None, title=title, size=(600, 600))
		self.draw_ui()
		# 使视图在中间显示
		self.Center()
		# 展示视图
		self.Show()
	
	def draw_ui(self):
		# 设置面板
		self.p = wx.Panel(self)
		# 设置垂直布局
		vbox = wx.BoxSizer(wx.VERTICAL)
		
		# 设置文字--单张图片原始路径
		l_img_sel = wx.StaticText(self.p, label='图片原始路径', style=wx.ALIGN_LEFT)
		# 设置字体样式
		l_img_sel.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
		# 添加进布局中
		vbox.Add(l_img_sel, 0, wx.ALL | wx.EXPAND, 6)
		
		# 第二行布局，横向，选择单张图片文件
		hbox_file = wx.BoxSizer(wx.HORIZONTAL)
		# 创建输入框
		self.tc_file = wx.TextCtrl(self.p, size=(400, 24))
		self.tc_file.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
		hbox_file.Add(self.tc_file, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
		# 创建按钮--选择文件
		btn_file = wx.Button(self.p, label='选择图片')
		btn_file.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
		# 绑定点击事件
		self.Bind(wx.EVT_BUTTON, self.sel_file, btn_file)
		hbox_file.Add(btn_file, 0, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
		vbox.Add(hbox_file, 0, wx.ALL | wx.EXPAND, 6)
		
		# 设置文字--图片文件夹原始路径
		l_img_dir_sel = wx.StaticText(self.p, label='文件夹原始路径', style=wx.ALIGN_LEFT)
		# 设置字体样式
		l_img_dir_sel.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
		# 添加进布局中
		vbox.Add(l_img_dir_sel, 0, wx.ALL | wx.EXPAND, 6)
		
		# 第四行布局，横向，选择文件夹
		hbox_dir = wx.BoxSizer(wx.HORIZONTAL)
		# 创建输入框
		self.tc_dir = wx.TextCtrl(self.p, size=(400, 24))
		self.tc_dir.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
		hbox_dir.Add(self.tc_dir, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
		# 创建按钮--选择文件夹
		btn_dir = wx.Button(self.p, label='选择文件夹')
		btn_dir.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
		# 绑定点击事件
		self.Bind(wx.EVT_BUTTON, self.sel_dir, btn_dir)
		hbox_dir.Add(btn_dir, 0, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
		# ----
		vbox.Add(hbox_dir, 0, wx.ALL | wx.EXPAND, 6)
		
		hbox_wh = wx.BoxSizer(wx.HORIZONTAL)
		# 设置提示--宽
		l_width = wx.StaticText(self.p, label='宽：', style=wx.ALIGN_LEFT)
		l_width.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
		hbox_wh.Add(l_width, 0, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
		
		# 设置输入框--宽
		self.tc_width = wx.TextCtrl(self.p, size=(120, 24))
		self.tc_width.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
		hbox_wh.Add(self.tc_width, 0, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
		
		# 设置提示--高
		l_height = wx.StaticText(self.p, label='高：', style=wx.ALIGN_LEFT)
		l_height.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
		hbox_wh.Add(l_height, 0, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
		
		# 设置输入框--高
		self.tc_height = wx.TextCtrl(self.p, size=(120, 24))
		self.tc_height.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
		hbox_wh.Add(self.tc_height, 0, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
		# ----
		vbox.Add(hbox_wh, 0, wx.ALL | wx.EXPAND, 6)
		
		# 设置文字--保存路径
		l_img_save = wx.StaticText(self.p, label='保存路径', style=wx.ALIGN_LEFT)
		# 设置字体样式
		l_img_save.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
		# 添加进布局中
		vbox.Add(l_img_save, 0, wx.ALL | wx.EXPAND, 6)
		
		# 设置保存路径
		hbox_save = wx.BoxSizer(wx.HORIZONTAL)
		# 创建输入框
		self.tc_save = wx.TextCtrl(self.p, size=(400, 24))
		self.tc_save.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
		hbox_save.Add(self.tc_save, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
		# 创建按钮--选择保存路径
		btn_file_save = wx.Button(self.p, label='选择保存路径')
		btn_file_save.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
		# 绑定点击事件
		self.Bind(wx.EVT_BUTTON, self.sel_dir_save, btn_file_save)
		hbox_save.Add(btn_file_save, 0, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
		# ----
		vbox.Add(hbox_save, 0, wx.ALL | wx.EXPAND, 6)
		
		# 执行行
		hbox_exc = wx.BoxSizer(wx.HORIZONTAL)
		# 单张图片压缩按钮
		btn_exc_img = wx.Button(self.p, label='压缩单张图片')
		btn_exc_img.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
		# 绑定点击事件
		self.Bind(wx.EVT_BUTTON, self.exc_img, btn_exc_img)
		hbox_exc.Add(btn_exc_img, 0, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
		# 批量压缩按钮
		btn_exc_batch = wx.Button(self.p, label='批量压缩')
		btn_exc_batch.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
		# 绑定点击事件
		self.Bind(wx.EVT_BUTTON, self.exc_batch, btn_exc_batch)
		hbox_exc.Add(btn_exc_batch, 0, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
		# ----
		vbox.Add(hbox_exc, 0, wx.ALL | wx.EXPAND, 6)
		
		# 将布局加载到面板上
		self.p.SetSizer(vbox)
	
	# 选择文件
	def sel_file(self, event):
		# 文件格式过滤器，这里将所有文件显示出来
		files_filter = "All files(*.*)|*.*"
		# 打开文件选择窗口
		file_dialog = wx.FileDialog(self, message="选择单张图片", wildcard=files_filter, style=wx.FD_OPEN)
		# 点击OK后，将路径显示到输入框中
		if file_dialog.ShowModal() == wx.ID_OK:
			# 在输入框中显示路径
			self.tc_file.SetLabel(file_dialog.GetPath())
		file_dialog.Destroy()
	
	# 选择文件夹
	def sel_dir(self, event):
		# 打开文件夹选择窗口
		dlg = wx.DirDialog(self, message="选择文件夹", style=wx.DD_DEFAULT_STYLE)
		# 点击OK
		if dlg.ShowModal() == wx.ID_OK:
			# 在输入框中显示文件夹路径
			self.tc_dir.SetLabel(dlg.GetPath())
		dlg.Destroy()
	
	# 选择保存路径
	def sel_dir_save(self, event):
		# 打开文件夹选择窗口
		dlg = wx.DirDialog(self, message="选择文件夹", style=wx.DD_DEFAULT_STYLE)
		# 点击OK
		if dlg.ShowModal() == wx.ID_OK:
			# 在输入框中显示文件夹路径
			self.tc_save.SetLabel(dlg.GetPath())
		dlg.Destroy()
	
	# 压缩单张图片
	def exc_img(self, event):
		result = ImgTool.img_cop(self=ImgTool, f=self.tc_file.GetLabel(), w=self.tc_width.GetLabel(), h=self.tc_height.GetLabel(), nf=self.tc_save.GetLabel())
		if result:
			wx.MessageDialog(self, '完成', caption='Result').ShowModal()
		else:
			wx.MessageDialog(self, '失败', caption='Result').ShowModal()
		pass
	
	# 批量压缩
	def exc_batch(self, event):
		print(self.tc_dir.GetLabel())
		pass


def main_show():
	app = wx.App()
	ImgToolUI()
	app.MainLoop()


main_show()
