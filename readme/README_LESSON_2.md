# 第二周作业

## 要求:

是用类视图完成用户的增删改查操作

## 实现：
> views代码:

```
class UserView(View):
    # 设置HTTP请求类型保留4种，增加一种LIST
    http_method_names = ['get', 'post', 'put', 'delete', 'list']

    # [GET]查询用户
    def get(self, request, *args, **kwargs):
        logger.debug("用户查询")
        id = request.GET.get('id')
        user = User.objects.get(id=id)
        return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email}, safe=False)

    # [POST]修改用户
    def post(self, request, *args, **kwargs):
        logger.debug("用户修改")
        uid = request.POST.get('id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.get(id=uid)
        user.set_password(password)
        user.username = username
        user.email = email
        user.save()
        return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email}, safe=False)

    # [DELETE]删除用户
    def delete(self, request, *args, **kwargs):
        logger.debug("用户删除")
        param = QueryDict(request.body)
        uid = param.get('id')
        user = User.objects.get(id=uid)
        user.delete()

        return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email}, safe=False)

    # [PUT]添加用户
    def put(self, request, *args, **kwargs):
        logger.debug("用户添加")
        data = QueryDict(request.body).dict()

        user = User.objects.create_user(**data)

        return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email}, safe=False)

    # [LIST]用户列表带分页
    def list(self, request, *args, **kwargs):
        logger.debug("用户列表")
        param_dict = QueryDict(request.body)
        per = 10
        page = int(param_dict.get("page", 1))

        queryset = User.objects.all().order_by('id')
        paginator = Paginator(queryset, per)
        if page < paginator.page_range[0]:
            page = paginator.page_range[0]
        elif page > paginator.page_range[-1]:
            page = paginator.page_range[-1]
        paginator.page(page)
        data = [{'id': user.id, 'username': user.username, 'email': user.email} for user in
                paginator.page(page).object_list]
        return JsonResponse(data, safe=False)
```

> 调用代码:

```
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
```

> 调用结果:
```
[PUT]添加用户成功： {"id": 113, "username": "oldold", "email": "oldold@test.com"}
[GET]查询用户成功： {"id": 113, "username": "oldold", "email": "oldold@test.com"}
[POST]修改用户成功： {"id": 113, "username": "newnew", "email": "newnew@test.com"}
[DELETE]删除用户成功： {"id": null, "username": "newnew", "email": "newnew@test.com"}
[LIST]分页查询数据: [{"id": 101, "username": "oldname", "email": "oldname@test.com"}, {"id": 102, "username": "oldname1", "email": "oldname1@test.com"}, {"id": 104, "username": "oldname2", "email": "oldname2@test.com"}, {"id": 105, "username": "oldname3", "email": "oldname3@test.com"}, {"id": 106, "username": "oldname4", "email": "oldname4@test.com"}, {"id": 107, "username": "oldname5", "email": "oldname5@test.com"}]

```