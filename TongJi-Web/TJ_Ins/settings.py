# -*- coding: utf-8 -*-
# @Time : 2020/11/21 14:45
# @File : settings.py
# @author : Dino
# 使用类组织配置

import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# win与linux数据库URI有所不同
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


# 基本配置
class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')

    # 关闭数据库警告信息
    SQLALCHEMY_TRACK_MODIFICATIONS = False

