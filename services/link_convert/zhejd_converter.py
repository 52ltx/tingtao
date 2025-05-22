# -*- coding: utf-8 -*-
# @Author  : lintingxue

import requests

from config.loader import CONFIG
from utils.logger import get_logger

logger = get_logger("zheJd")
config = CONFIG['zheJd']
ZJD_APP_KEY = config['appKey']
ZJD_SID = config['sid']
ZJD_UNION_ID = config['unionId']

class ZheJDConverter:
    def __init__(self):
        self.req = requests.Session()
        self.appKey = ZJD_APP_KEY
        self.sid = ZJD_SID
        self.unionId = ZJD_UNION_ID

    def convert_high_commission_links_batch(self, content):
        """
        批量高佣转链API（文案）接口---将第三方京东文案转成自己的京东文案，只替换链接，同时支持淘宝、京东、拼多多、苏宁、唯品会、美团等平台 。
        :param content:
        :return:
        """
        logger.info(f"批量高佣转链开始转链：{content}")
        url = "https://api.zhetaoke.com:10001/api/open_gaoyongzhuanlian_tkl_piliang.ashx"
        payload = {
            "appkey": self.appKey,
            "sid": self.sid,
            "pid": "0",
            "tkl": content,  # 商品ID
            "unionId": self.unionId,
        }
        try:
            response = self.req.post(url, data=payload)
            logger.info(f"转换日志：{response.json()}")
            return response.json()
        except requests.RequestException as e:
            logger.error(f"转链失败：{e}")
            return {"error": "Request failed", "message": str(e)}
