# coding=utf8


"""
美翻项目配置文件，其中分开发，生产，测试三个版本

Created on 2018-10-25 by Varwey
"""

from personal_blog.config import  development

__all__ = ['setting']

import os

# 环境配置字典，可随时添加配置环境读取不同配置文件
setting_dict = {
    "development": lambda: development,

}

# current_evn = os.environ.get("BEAUTY_FAN_ENV") or "development"
current_evn = "development"

setting = setting_dict.get(current_evn)()

del development

