import requests

url_login = 'http://127.0.0.1:8000/dashboard/login/'
print('login_url:', url_login)
data = {'id': 'll', 'pw': '123'}
res = requests.post(url_login, data)
print(data)
print(res.text)

data = {'id': 'll', 'pw': '1231'}
res = requests.post(url_login, data)
print(data)
print(res.text)
