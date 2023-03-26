import os
import json
import pypinyin

# 读取大学名字列表
with open('S:\\pachong\\Tieba_Spider\\school_list_output.txt', 'r', encoding='utf-8') as f:
    universities = f.read().strip().split('，')  # 注意使用中文逗号

# 生成大学名字缩写的字典
university_abbreviations = {}
for university in universities:
    abbreviation = ''
    for p in pypinyin.pinyin(university, style=pypinyin.NORMAL):
        abbreviation += p[0][0]
    university_abbreviations[university] = abbreviation

# 保存字典到 json 文件
with open('S:\\pachong\\Tieba_Spider\\university_abbreviations.json', 'w', encoding='utf-8') as f:
    json.dump(university_abbreviations, f, ensure_ascii=False, indent=4)
