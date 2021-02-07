import requests
import re

# 获取页面全部HTML信息
res = requests.get('https://yuncode.net/')
res.encoding = 'utf-8'
html = res.text
# print(html)

# 将HTML信息写入文件
f = open(r"C:\Users\jerry\Desktop\web_html.txt", 'w+', encoding="utf-8")  # w+:以追加方式打开文件
f.write(html)
f.close()

# 读取HTML信息
f = open(r"C:\Users\jerry\Desktop\web_html.txt", 'r+', encoding="utf-8")  # r+:以读写方式打开文件
data = f.readlines()  # data是数组类型

count = 0  # 初始化计数，计算获取的帖子的数量；也可以最后直接获取数组的长度
url_list = []  # 用于存储帖子url
title_list = []  # 用于存储帖子标题

search = '<a class="ft-a-title"'  # 查找条件，见上述分析

# 逐行读取HTML信息
for line in range(len(data)):
    if search in data[line]:
        line_html = data[line] + data[line + 1]  # 此句关键，见上述分析
        # print(line_html)

        # 正则表达式获取帖子URL
        res_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
        link = re.findall(res_url, line_html, re.I | re.S | re.M)
        for url in link:
            print(url)
            url_list.append(url)  # 将url加入数组

        # 正则表达式获取帖子标题
        res = r'<a .*?>(.*?)</a>'
        text = re.findall(res, line_html, re.I | re.S | re.M)
        for content in text:
            print(content)
            title_list.append(content)  # 将标题加入数组

        # 匹配查找成功，计数+1
        count += 1
    else:
        continue

# 最终统计查找的帖子数量
print('当前页共计 ' + str(count) + ' 篇帖子')

# 打印所有url与标题
print(url_list)
print(title_list)

# 最终务必记得关闭文件
f.close()
