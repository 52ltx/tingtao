import os
import re
import time
from datetime import datetime

# -*- coding: utf-8 -*-
# @Author  : lintingxue
import requests

from config.loader import CONFIG
from services.bot.wx_bot import WXUi
from services.link_convert.parser import parse_content
from utils.helpers import create_dir, save_pic, delete_file


class LanPixia:
    def __init__(self):
        self.config = CONFIG["lanpixia"]
        self.req = requests.Session()
        self.host = "https://www.lanpixia.com"
        self.req.headers = {
            "x-appid":"2104152554",
            "Referer": "https://www.lanpixia.com/groupDetail/?platform=pinduoduo&source_id=201&sourceType=group",
        }
        self.msg_id_list = {}   # 消息id列表
        create_dir(os.path.join(os.getcwd(), "tmp"))
        self.wx = WXUi()

    def group_preview_list(self, source_id="201", send_name="", position="pre"):
        """
        获取群聊预览列表
        :param source_id: 群聊id
        :param position: 预览位置，pre：前，next：后
        :return:
        """
        url = f"{self.host}/backend/weixin/group_preview_list?source_id={source_id}&position={position}"
        res = self.req.get(url)
        if res.status_code != 200:
            return {"code": 500, "msg": "请求失败"}
        else:
            res_json = res.json()
            if res_json['status'] == 20:
                result = res_json['result']
                if self.msg_id_list.get(source_id):
                    for item in result:
                        msg_type = item['msg_type']
                        content = item['content']
                        if item['new_msgid'] not in self.msg_id_list[source_id]:
                            send_create = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(item['send_create'])))
                            if msg_type == "1":
                                # 文本消息
                                new_content = parse_content(content)
                                print(send_create, new_content)
                                self.wx.send_text_msg(send_name, new_content)
                            elif msg_type == "3":
                                # 图片消息
                                print(item['bigurl'])
                                pic_path = save_pic(f"https:{item['bigurl']}")
                                self.wx.send_img_msg(send_name, [pic_path])
                                delete_file(pic_path)
                            elif msg_type == "47":
                                # 图片消息
                                print(item['bigurl'])
                                pic_path = save_pic(item['bigurl'])
                                self.wx.send_img_msg(send_name, [pic_path])
                                delete_file(pic_path)
                            self.msg_id_list[source_id].append(item['new_msgid'])
                else:
                    self.msg_id_list[source_id] = []
                    for item in result:
                        self.msg_id_list[source_id].append(item['new_msgid'])
        return res.json()