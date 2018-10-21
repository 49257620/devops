import requests

url = 'http://127.0.0.1:8000/dashboard/user/'

print(requests.request('GET', url).text)
print(requests.request('POST', url).text)
print(requests.request('DELETE', url).text)
print(requests.request('PUT', url).text)
print(requests.request('LIST', url).text)

