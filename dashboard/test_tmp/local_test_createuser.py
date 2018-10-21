# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

import requests

url = 'http://127.0.0.1:8000/dashboard/user/'

data = {'password': '123456', 'username': 'llww10', 'email': 'test@test.com'}

# res = requests.post(url, data)
res = requests.put(url, data)

print(res.text)
