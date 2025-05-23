# -*- coding: utf-8 -*-
# @Author  : lintingxue
class UserSession:
    def __init__(self, user_id):
        from services.link_convert.dataoke_converter import DaTaoKeConverter
        self.user_id = user_id
        self.converter = DaTaoKeConverter()
        self.goods_list = []
        self.current_index = 0

    def query_goods(self, keyword, pageId=1, pageSize=20, type=0):
        result = self.converter.query_goods(type, pageId, pageSize, keyword)
        if result.get("code") == 200 and "data" in result:
            self.goods_list = result["data"].get("list", [])
            self.current_index = 0
            return True
        else:
            self.goods_list = []
            return False

    def get_next_good(self):
        if self.current_index < len(self.goods_list):
            good = self.goods_list[self.current_index]
            self.current_index += 1
            return good
        else:
            return None

