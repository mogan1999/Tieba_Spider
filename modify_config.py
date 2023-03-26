import json
import sys

university = sys.argv[1]

# 读取 json 文件
with open('config.json', 'r+', encoding='utf-8', newline='') as f:
    config = json.load(f)
    # 清空字典
    config['MYSQL_DBNAME'] = {}
    # 修改配置项
    config['MYSQL_DBNAME'][university] = f'{university}data'
    # 将文件指针移动到开头
    f.seek(0)
    # 保存修改后的 json 文件
    json.dump(config, f, indent=4,ensure_ascii=False)
    # 删除文件指针之后的内容
    f.truncate()