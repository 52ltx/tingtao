# 听淘 - 淘客导购转链发单工具

## 项目简介
TingTao（听淘）是一个淘客转链导购发单工具，支持淘宝、京东、拼多多等平台的商品链接转链功能，并支持微信群转发和私聊群聊导购查券。发单可拓展发送至自定义平台，如企业微信、QQ群、钉钉群等。

## 主要功能
- ✅ 已实现功能：
  - 淘宝/天猫/拼多多商品链接转链（通过大淘客API）
  - 京东商品链接转链（通过折京东API）
  - 监控蓝皮虾商品转发到指定私聊/群聊

- ⏳ 开发中功能：
  - A群转发到B群
  - 导购查券

## wxauto环境要求
|  环境  | 版本 |
| :----: | :--: |
|  微信  | [![Wechat](https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1-3.9.11.X-07c160?logo=wechat&logoColor=white)](https://github.com/tom-snow/wechat-windows-versions/releases/download/v3.9.11.17/WeChatSetup-3.9.11.17.exe) |
| Python | [![Python](https://img.shields.io/badge/Python-3.X-blue?logo=python&logoColor=white)](https://www.python.org/) **(不支持3.7.6和3.8.1)**|

## 安装步骤
1. 克隆项目仓库
```bash
git clone https://github.com/your-repo/tingtao.git
cd tingtao
```
2. 安装依赖
```bash
pip install -r requirements.txt
```
3. 配置设置
复制 settings.yml.bak 为 settings.yml 并填写您的API密钥等配置信息
```bash
cp settings.yml.bak settings.yml
```
4. 运行项目
```bash
python main.py
```
## 项目结构
```bash
tingtao/
├── main.py              # 主程序入口
├── utils/               # 工具模块
├── settings.yml.bak     # 配置文件模板
├── config/
│   └── loader.py        # 配置加载器
├── settings.yml         # 配置文件
├── requirements.txt     # 依赖列表
└── logs/                # 日志目录