import json
import os
import random
import time

# 获取当前日期
date_str = time.strftime('%Y%m%d', time.localtime())

# 读取大学名字列表
with open('school_list_output.txt', 'r', encoding='utf-8') as f:
    universities = f.read().strip().split('，')  # 注意使用中文逗号

# 生成批处理命令列表
commands = []
for university in universities:
    command = f'scrapy run {university} {university}data -p 1 10'  
    # 修改 json 文件
    config_modify_cmd = f'python modify_config.py {university}'
    commands.append(f'{config_modify_cmd};\n{command};')

# 生成 bash 脚本文件
with open(f'getdata{date_str}.sh', 'w', encoding='utf-8', newline='') as f:
    # 添加激活虚拟环境的代码
    f.write('#!/bin/bash\n')
    f.write('source /usr/local/anaconda3/bin/activate tieba\n\n')
    f.write('cd /home/raoziyang/Tieba_Spider\n\n')
    for i in range(2):
        for command in commands:
            f.write(f'{command}\n')  # 写入命令
            wait_time = random.randint(7200, 7300)  # 生成3600-4000之间的随机整数
            f.write(f'echo current task finished at:\n')
            f.write(f'date\n')
            f.write(f'echo "waiting {wait_time}s for next task......"\n') # 打印语句
            f.write(f'sleep {wait_time}\n')  # 使用 sleep 命令等待随机整数秒
    f.write('echo "all done"\n')