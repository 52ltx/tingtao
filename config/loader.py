# -*- coding: utf-8 -*-
# @Author  : lintingxue
import yaml
import os

def load_config(path=None):
    if not path:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "settings.yml")

    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# 提前加载一份全局配置（可选）
CONFIG = load_config()