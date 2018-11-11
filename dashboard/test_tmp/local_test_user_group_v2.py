# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’



"""
url = 'http://127.0.0.1:8000/userGroups/'

res = requests.post(url, json={"uid":3, "gid":1})
print('新增：', res.text)
"""

import requests, json

url = 'http://127.0.0.1:8000/userGroups/1/'

res = requests.delete(url, json={"uid":3, "gid":1})
print('delete删除：', res.text)




