import re
from bs4 import BeautifulSoup

# 打开HTML文件
with open('S:\pachong\Tieba_Spider\school_list.txt', 'r', encoding='utf-8') as html_file:
    # 解析HTML文件
    soup = BeautifulSoup(html_file, 'html.parser')

# 使用正则表达式查找所有以“大学”和“学院”结尾的字符串
matched_strings = []
for string in soup.stripped_strings:
    if re.search(r'(大学|学院)$', string):
        matched_strings.append(string)

# 如果匹配成功，则将匹配到的字符串以指定的格式写入输出文件
if len(matched_strings) > 0:
    with open('S:\pachong\Tieba_Spider\school_list_output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(matched_strings[0])

        for i in range(1, len(matched_strings)):
            # 在字符串之间添加逗号和空格
            output_file.write('，' + matched_strings[i])

        output_file.write('。')
else:
    print('没有找到匹配的字符串。')