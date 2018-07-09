#!/usr/bin/evn python
# -*-coding : utf-8 -*-

import copy
import random

import numpy as np
import wx

"""
完成的一个数独游戏的小程序，学习Python迈出的第一步
"""
def init_new_data():
    one_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    two_list = []
    three_list = []
    four_list = []
    five_list = []
    six_list = []
    seven_list = []
    eight_list = []
    nine_list = []
    random.shuffle(one_list)
    np_one_list = np.array(one_list)
    one = np.split(np_one_list, 3)
    two_list.append(one[1])
    three_list.append(one[2])
    two_list.append(one[2])
    three_list.append(one[0])
    two_list.append(one[0])
    three_list.append(one[1])
    two_list = np.ravel(two_list, order="A")
    three_list = np.ravel(three_list, order="A")
    col_one = np.transpose(one)
    four_list.append(col_one[1])
    seven_list.append(col_one[2])
    four_list.append(col_one[2])
    seven_list.append(col_one[0])
    four_list.append(col_one[0])
    seven_list.append(col_one[1])
    four_list = np.ravel(four_list, order="F")
    seven_list = np.ravel(seven_list, order="F")
    three = np.split(three_list, 3)
    col_three = np.transpose(three)
    six_list.append(col_three[1])
    nine_list.append(col_three[2])
    six_list.append(col_three[2])
    nine_list.append(col_three[0])
    six_list.append(col_three[0])
    nine_list.append(col_three[1])
    six_list = np.ravel(six_list, order="F")
    nine_list = np.ravel(nine_list, order="F")
    five_list.append(two_list[2])
    five_list.append(two_list[0])
    five_list.append(two_list[1])
    five_list.append(six_list[0])
    five_list.append(six_list[1])
    five_list.append(six_list[2])
    five_list.append(seven_list[0])
    five_list.append(seven_list[1])
    five_list.append(seven_list[2])
    eight_list.append(one_list[4])
    eight_list.append(one_list[5])
    eight_list.append(one_list[3])
    eight_list.append(seven_list[6])
    eight_list.append(seven_list[7])
    eight_list.append(seven_list[8])
    eight_list.append(six_list[3])
    eight_list.append(six_list[4])
    eight_list.append(six_list[5])

    all_list = []
    all_list.append(np_one_list)
    all_list.append(two_list)
    all_list.append(three_list)
    all_list.append(four_list)
    all_list.append(five_list)
    all_list.append(six_list)
    all_list.append(seven_list)
    all_list.append(eight_list)
    all_list.append(nine_list)
    all_list = np.array(all_list)

    return all_list


olds = []
news = []


class MySuduku(wx.Frame):

    def __init__(self, parent, title="My Suduku", ndarrs=[]):
        super(MySuduku, self).__init__(parent, title=title, size=(500, 500))
        self.init_ui(ndarrs)
        self.Centre()
        self.Show()

    def init_ui(self, ndarrs):
        p = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        gs = wx.GridSizer(3, 3, 4, 4)
        for i in range(0, 9):
            news.append(ndarrs[i])
            ges = wx.GridSizer(3, 3, 4, 4)
            for j in range(0, 9):
                num = random.randint(0, 8)
                number = random.randint(0, 8)
                new = random.randint(0, 8)
                n = random.randint(0, 8)
                if n * new > num * number:
                    btn = str(ndarrs[i][j])
                    my_btn = wx.Button(p, label=btn, size=(40, 40))
                    my_btn.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD, False))
                    my_btn.SetBackgroundColour('white')
                    my_btn.Enabled = False
                else:
                    news[i][j] = 0
                    my_btn = wx.Button(p, label=str(ndarrs[i][j]), size=(40, 40))
                    my_btn.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
                    ints = str(i) + str(j)
                    my_btn.SetName(ints)
                    my_btn.SetForegroundColour('white')
                    my_btn.SetBackgroundColour('white')
                    # 设置点击事件
                    self.Bind(wx.EVT_BUTTON, self.OnClick, my_btn)
                ges.Add(my_btn, 0, wx.EXPAND)
            gs.Add(ges, 0, wx.EXPAND)
        box.Add(gs, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND)

        my_btn_restart = wx.Button(p, label="Restart", size=(60, 40))
        my_btn_restart.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        my_btn_restart.SetForegroundColour('red')
        self.Bind(wx.EVT_BUTTON, self.OnRestart, my_btn_restart)
        box.Add(my_btn_restart, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND)

        my_btn_ok = wx.Button(p, label="OK", size=(60, 40))
        my_btn_ok.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        my_btn_ok.SetForegroundColour('red')
        self.Bind(wx.EVT_BUTTON, self.OnOk, my_btn_ok)
        box.Add(my_btn_ok, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND)

        p.SetSizer(box)

    def OnClick(self, event):
        number = event.GetEventObject().GetName()
        x = 0
        y = 0
        if len(number) == 1:
            x = 0
            y = number[0]
        elif len(number) == 2:
            x = number[0]
            y = number[1]
        MyDialog(self, title="请选择", btn=event.GetEventObject(), x=x, y=y).ShowModal()

    def OnRestart(self, event):
        self.Close(True)
        main()

    def OnOk(self, event):
        one_news = np.ravel(news, order="A")
        one_olds = np.ravel(olds, order="A")
        result = one_news == one_olds
        # 可以替换为np.all()函数进行判断，数组元素是否全部是True
        if np.sum(result == 0) == 0:
            wx.MessageDialog(self, 'Incredible！', caption='Result').ShowModal()
        else:
            wx.MessageDialog(self, 'MDZZ！', caption='Result').ShowModal()


class MyDialog(wx.Dialog):
    my_btn = None
    xx = 0
    yy = 0

    def __init__(self, parent, title, btn, x, y):
        super(MyDialog, self).__init__(parent, title=title, size=(200, 200))
        self.my_btn = btn
        self.xx = int(x)
        self.yy = int(y)

        panel = wx.Panel(self)
        gs = wx.GridSizer(3, 3, 4, 4)
        for i in range(1, 10):
            btn = str(i)
            my_btn_in = wx.Button(panel, label=btn, size=(40, 40))
            my_btn_in.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD, False))
            gs.Add(my_btn_in, 0, wx.EXPAND)
            self.Bind(wx.EVT_BUTTON, self.OnClicked, my_btn_in)
        panel.SetSizer(gs)
        self.Centre()

    def OnClicked(self, event):
        self.my_btn.SetLabel(event.GetEventObject().GetLabel())
        self.my_btn.SetForegroundColour('red')
        news[self.xx][self.yy] = int(event.GetEventObject().GetLabel())
        self.Destroy()


def main():
    mList = init_new_data()
    olds = copy.deepcopy(mList)
    app = wx.App()
    MySuduku(None, ndarrs=mList)
    app.MainLoop()


main()
