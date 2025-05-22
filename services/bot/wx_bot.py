# -*- coding: utf-8 -*-
# @Author  : lintingxue
from wxauto import WeChat


class WXUi:
    def __init__(self):
        self.wx = WeChat()

    def send_text_msg(self, who, msg):
        self.wx.SendMsg(msg=msg, who=who)

    def send_img_msg(self, who, files):
        self.wx.SendFiles(filepath=files, who=who)