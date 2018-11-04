# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

import requests, json

"""
url = 'http://127.0.0.1:8000/idcs/'

# 添加用户组
res = requests.post(url, json={'name': '北京机房16', 'address': '北京5', 'phone': '12345678', 'email': '123@123.com'})
print('添加：', res.text)


idc = json.loads(res.text)
# print(idc)

url = 'http://127.0.0.1:8000/idcs/' + str(idc['id']) + '/'

res = requests.put(url, {'name': '北京机房00-修改', 'address': '北京1-修改', 'phone': '123456780', 'email': '000@123.com'})
print('修改：', res.text)

url = 'http://127.0.0.1:8000/idcs/' + str(idc['id']) + '/'
res = requests.delete(url)
print('删除：', res.text)

url = 'http://127.0.0.1:8000/idcs/1/'

res = requests.put(url, json={'name': '北京机房22', 'address': '北京22-修改', 'phone': '123456780', 'email': '222@123.com'})
print('修改：', res.text)

url = 'http://127.0.0.1:8000/idcs/15/'
res = requests.delete(url)
print('删除：', res.status_code)
"""

url = 'http://127.0.0.1:8000/idcs/1/'

res = requests.put(url, json={'name': '北京机房22', 'address': '北京22-修改', 'phone': '123456780', 'email': '222@123.com'})
print('修改：', res.text)




