# encoding: utf-8
# Author: LW
import requests, json

url = 'http://127.0.0.1:8000/dashboard/group/list/'
res = requests.get(url)
print('获取全部组列表：', res.text)

url = 'http://127.0.0.1:8000/dashboard/groupuser/?gid=1'
res = requests.get(url)
print('获取组成员列表：', res.text)

url = 'http://127.0.0.1:8000/dashboard/usergroup/?uid=4'
res = requests.get(url)
print('获取用户组列表：', res.text)

url = 'http://127.0.0.1:8000/dashboard/usergroup/add/'

# 添加用户组
res = requests.post(url, {'uid': 8, 'gid': 1})
print('添加用户组关系：', res.text)

url = 'http://127.0.0.1:8000/dashboard/usergroup/del/'

# 删除用户组
res = requests.post(url, {'uid': 8, 'gid': 1})
print('删除用户组关系：', res.text)

# 添加新组

url = 'http://127.0.0.1:8000/dashboard/group/add/'
res = requests.post(url, {'gname': 'group5'})
print('添加新组：', res.content.decode('utf-8'))
