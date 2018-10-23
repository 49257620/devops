# encoding: utf-8
# Author: LW
import requests, json

url = 'http://127.0.0.1:8000/dashboard/user/'

# 添加用户
res = requests.put(url, {'password': '123456', 'username': 'oldold', 'email': 'oldold@test.com'})
print('[PUT]添加用户成功：', res.text)

user = json.loads(res.text)

# 查询用户
res = requests.get(url, {'id': user['id']})
print('[GET]查询用户成功：', res.text)

# 修改用户
res = requests.post(url, {'id': user['id'], 'password': '111111', 'username': 'newnew', 'email': 'newnew@test.com'})
print('[POST]修改用户成功：', res.text)

# 删除用户
res = requests.delete(url, data={'id': user['id']})
print('[DELETE]删除用户成功：', res.text)

# 用户列表带分页
res = requests.request('list', url, data={"page": 1000})
print("[LIST]分页查询数据:", res.text)
