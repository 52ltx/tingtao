# -*- coding: utf-8 -*-
# @Author  : lintingxue

import hashlib
import random
import time

import requests

from config.loader import CONFIG
from utils.logger import get_logger

logger = get_logger("dataoke")
config = CONFIG['dataoke']
DTK_APP_KEY = config['appKey']
DTK_APP_SECRET = config['appSecret']

def generate_sign():
    # 生成sign
    nonce = str(random.randint(100000, 999999))  # 6位随机数
    timer = str(int(time.time() * 1000))  # 毫秒级时间戳
    # 组装验签字符串
    sign_str = f"appKey={DTK_APP_KEY}&timer={timer}&nonce={nonce}&key={DTK_APP_SECRET}"
    # MD5加密并转为大写
    sign_ran = hashlib.md5(sign_str.encode()).hexdigest().upper()
    return nonce, timer, sign_ran


def _build_common_params(extra_params=None):
    """
    构建通用请求参数
    :param extra_params: 额外参数字典
    :return: 完整参数字典
    """
    nonce, timer, sign_ran = generate_sign()
    params = {
        "appKey": DTK_APP_KEY,
        "appSecret": DTK_APP_SECRET,
        "nonce": nonce,
        "timer": timer,
        "signRan": sign_ran
    }
    if extra_params:
        params.update(extra_params)
    return params


class DaTaoKeConverter:
    def __init__(self):
        self.req = requests.Session()

    def get_privilege_link(self, goods_id):
        """
        高效转链
        :param goods_id:
        :return: 转链结果
        """
        logger.info(f"高效转链开始转链：{goods_id}")
        url = "https://openapi.dataoke.com/api/tb-service/get-privilege-link"
        params = _build_common_params({
            "version": "1.3.1",
            "goodsId": goods_id
        })
        try:
            response = self.req.get(url, params=params)
            logger.info(f"转换日志：{response.json()}")
            return response.json()
        except requests.RequestException as e:
            logger.error(f"转链失败：{e}")
            return {"error": "Request failed", "message": str(e)}

    def parse_content(self, content):
        """
        淘系万能解析转链
        :param content:
        :return:转链结果
        """
        logger.info(f"淘系万能解析转链开始转链：{content}")
        url = "https://openapi.dataoke.com/api/tb-service/parse-content"
        params = _build_common_params({
            "version": "1.0.0",
            "content": content
        })
        try:
            response = self.req.get(url, params=params)
            logger.info(f"转换日志：{response.json()}")
            return response.json()
        except requests.RequestException as e:
            logger.error(f"转链失败：{e}")
            return {"error": "Request failed", "message": str(e)}

    def parse_clipboard_content(self, content):
        """
        剪贴板内容识别接口
        :param content: 剪贴板原始内容
        :return: 转链结果
        """
        logger.info(f"剪切板识别开始转链：{content}")
        url = "https://openapi.dataoke.com/api/dels/kit/contentParse"
        params = _build_common_params({
            "version": "1.0.0",
            "content": content
        })
        try:
            response = self.req.get(url, params=params)
            logger.info(f"转换日志：{response.json()}")
            return response.json()
        except requests.RequestException as e:
            logger.error(f"转链失败：{e}")
            return {"error": "Request failed", "message": str(e)}
    def query_goods(self, type,pageId,pageSize,keyword):
        """
        超级搜索查询商品列表
        :param type:    搜索类型：0-综合结果，1-大淘客商品，2-联盟商品
        :param pageId:  请求的页码，默认参数1
        :param pageSize:每页条数，默认为20，最大值100
        :param keyword: 关键词搜索
        :return:
        """

        url = "https://openapi.dataoke.com/api/goods/list-super-goods"
        params = _build_common_params({
            "version": "1.3.0",
            "type": type,
            "pageId": pageId,
            "pageSize": pageSize,
            "keyWords": keyword
        })
        logger.info(f"开始搜索：{params}")
        try:
            response = self.req.get(url, params=params)
            logger.info(f"搜索结果：{response.json()}")
            return response.json()
        except requests.RequestException as e:
            logger.error(f"转链失败：{e}")
            return {"error": "Request failed", "message": str(e)}

if __name__ == '__main__':
    converter = DaTaoKeConverter()
    converter.query_goods(type=0,pageId=1,pageSize=1,keyword="半袖")
