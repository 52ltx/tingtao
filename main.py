# 创建线程
# import threading
#
# from services.lanpixia import start_lanpixia
#
# lanpixia_thread = threading.Thread(target=start_lanpixia, daemon=True)
#
# # 启动线程
# lanpixia_thread.start()
#
# print("主线程继续执行其他任务...")
# 主线程可以继续做其他事，或者等待退出
from services.goods_router import handle_user_query

if __name__ == '__main__':
    print(handle_user_query("user_1", "手机"))
    print(handle_user_query("user_1", "手机"))  # 第二条
    print(handle_user_query("user_2", "电脑"))  # 用户2第一次查询