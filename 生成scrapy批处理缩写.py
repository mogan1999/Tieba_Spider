import os
import time
import json
import random

# 获取当前日期
date_str = time.strftime('%Y%m%d', time.localtime())

# 读取大学名字列表
with open('S:\\pachong\\Tieba_Spider\\school_list_output.txt', 'r', encoding='utf-8') as f:
    universities = f.read().strip().split('，')  # 注意使用中文逗号

# 读取大学名字与中文缩写的映射关系
with open('S:\\pachong\\Tieba_Spider\\university_abbreviations.json', 'r', encoding='utf-8') as f:
    university_abbr = json.load(f)

# 生成批处理命令列表
commands = []
for university in universities:
    abbr = university_abbr.get(university, '')
    command = f'scrapy run {university} {abbr}{date_str}data -p 1 12'  
    # 修改 json 文件
    config_modify_cmd = f'python modify_config.py {university}'
    commands.append(f'{config_modify_cmd}&&{command} ')

# 生成批处理文件
with open(f'S:\\pachong\\Tieba_Spider\\batch{date_str}.bat', 'w', encoding='ansi') as f:
    # 切换到虚拟环境tieba
    f.write('call activate tieba\n')

    # 切换工作目录到S:\pachong\Tieba_Spider
    f.write('cd /d S:\\pachong\\Tieba_Spider\n')

    for command in commands:
        f.write(f'{command}\n')  # 写入命令
        wait_time = random.randint(3600, 3800)  # 生成3600-4000之间的随机整数
        f.write(f'timeout /t {wait_time}\n')  # 使用 timeout 命令等待随机整数秒
