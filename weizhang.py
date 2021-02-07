#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib
from urllib import urlencode


# ----------------------------------
# 违章高发地调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/91
# ----------------------------------

def main():
    # 配置您申请的APPKey
    appkey = "*********************"

    # 1.检索周边违章高发地
    request1(appkey, "GET")


# 检索周边违章高发地
def request1(appkey, m="GET"):
    url = "http://v.juhe.cn/wzpoints/query"
    params = {
        "lat": "",  # 纬度,如：31.335005
        "lon": "",  # 经度，如：120.617183
        "page": "",  # 页数，默认:1
        "pagesize": "",  # 每次返回条数，默认20，最大50
        "r": "",  # 检索半径，默认：500，最大2000
        "key": appkey,  # 应用APPKEY(应用详细页查询)

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


if __name__ == '__main__':
    main()
