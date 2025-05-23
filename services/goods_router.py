# -*- coding: utf-8 -*-
# @Author  : lintingxue
from services.session.user_session import UserSession
from services.session import user_sessions

def handle_user_query(user_id, keyword):
    """
    处理用户查询商品的请求
    :param user_id: 用户唯一标识（如微信ID）
    :param keyword: 查询关键词
    :return: 返回下一条商品信息或提示信息
    """
    if user_id not in user_sessions:
        user_sessions[user_id] = UserSession(user_id)

    session = user_sessions[user_id]

    if not session.goods_list or session.current_index >= len(session.goods_list):
        success = session.query_goods(keyword)
        if not success:
            return {"message": "未找到相关商品，请尝试其他关键词"}

    good = session.get_next_good()
    if good:
        return {"good": good}
    else:
        return {"message": "当前无更多商品，请尝试刷新或更换关键词"}