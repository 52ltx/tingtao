# -*- coding: utf-8 -*-
# @Author  : lintingxue
import re

from .dataoke_converter import DaTaoKeConverter
from .zhejd_converter import ZheJDConverter

datk = DaTaoKeConverter()
zjd = ZheJDConverter()

def parse_content(content: str) -> str:
    """统一处理内容中的链接并进行转链替换"""
    if re.search(r"pinduoduo\.com|yangkeduo.com", content, re.IGNORECASE):
        url_pattern = r'https?://[a-zA-Z0-9-_.]+(?:/[a-zA-Z0-9-_/?&=]*)?'
        urls = re.findall(url_pattern, content)
        for url in urls:
            result = datk.parse_clipboard_content(url)
            if result.get("msg") == "成功v2" and result.get("data").get("parsedContent"):
                content = content.replace(url, result['data']['parsedContent'])
    elif re.search(r"jd\.com|3\.cn", content, re.IGNORECASE):
        result = zjd.convert_high_commission_links_batch(content)
        if result.get("status") == 200:
            content = result['content']
    else:
        result = datk.parse_clipboard_content(content)
        if result.get("msg") == "成功v2" and result.get("data").get("parsedContent"):
            content = result['data']['parsedContent']
    return content