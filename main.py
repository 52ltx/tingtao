import time
from datetime import datetime

from services.lanpixia import LanPixia

# from services.link_convert.parser import parse_content
#
# old_content = '''
# 先锁单，再犹豫!!!
# 补贴5.5虹包！=12.8亓，
# 任选男女都有，Artsdon
# 阿仕顿棉100%纯棉短袖T恤，
# /U4tkVkdwJab// HU108
# '''
#
# new_content = parse_content(old_content)
# print(new_content)
lp = LanPixia()
lp.wx.send_text_msg("文件传输助手", "蓝皮虾开始监听")
while True:
    # 多线程启动
    for config in lp.config['forward']:
        source_id = config['source_id']
        send_group_id = config['send_name']
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}-开始执行", source_id, send_group_id)
        lp.group_preview_list(source_id, send_group_id, "pre")
    # lp.group_preview_list(source_id="444", position="pre")
    time.sleep(lp.config['frequen cy'])