# -*- coding: utf-8 -*-
# @Time    : 10/4/2020 5:16 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: log.py
# @Software: PyCharm
import os
import logging

# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Log等级总开关

# 第二步，创建一个handler，用于写入日志文件
if "log" not in os.listdir():
    os.mkdir(os.path.join(os.getcwd(),"log"))
logfile = './log/logger.txt'
fh = logging.FileHandler(logfile, mode='a')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)  # 输出到console的log等级的开关

# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，将logger添加到handler里面
# logger.addHandler(fh)
logger.addHandler(ch)

# 日志
# logger.debug('this is a logger debug message')
# logger.info('this is a logger info message')
# logger.warning('this is a logger warning message')
# logger.error('this is a logger error message')
# logger.critical('this is a logger critical message')
