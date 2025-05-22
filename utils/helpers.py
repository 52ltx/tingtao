import os
import re

import requests


def save_pic(image_url, save_path=None):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # 检查请求是否成功
        # 如果未指定保存路径，则保存到当前目录下，文件名从URL中提取
        if save_path is None:
            if "wechat.lanpixia.com" in image_url:
                file_name = f"{os.path.basename(image_url)}.png"
            elif "qq.com" in image_url:
                filekey = re.findall(r"filekey=(.*?)&", image_url,re.S)
                if len(filekey)>0:
                    file_name = f"{filekey[0]}.gif"
                else:
                    # 随机生成文件名
                    file_name = f"{os.urandom(16)}.png"
            else:
                file_name = os.path.basename(image_url)
            tmp_path = os.path.join(os.getcwd(), "tmp")
            save_path = os.path.join(tmp_path, file_name)

        # 将图片内容写入本地文件
        with open(save_path, 'wb') as file:
            file.write(response.content)

        # 返回保存的图片的绝对路径
        return os.path.abspath(save_path)

    except requests.exceptions.RequestException as e:
        print(f"下载图片时出错：{e}")
        return None

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path

# 删除文件
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"文件 {file_path} 已删除")
    else:
        print(f"文件 {file_path} 不存在")