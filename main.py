# 创建线程
import threading

from services.lanpixia import start_lanpixia

lanpixia_thread = threading.Thread(target=start_lanpixia, daemon=True)

# 启动线程
lanpixia_thread.start()

print("主线程继续执行其他任务...")
# 主线程可以继续做其他事，或者等待退出