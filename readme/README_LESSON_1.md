# 第一周作业

## 要求:

创建100个用户

使用函数视图写一个功能，以json格式返回所有的用户信息，

选做：对用户列表进行分页

## 实现：
> 创建100个用户:

```
# 在django shell 中执行一下代码，插入100个用户（可参考代码 tmp/user_add.py）
from django.contrib.auth.models import User
for x in range(100):
    User.objects.create_user('user' + str(x + 1), 'email' + str(x + 1) + '@email.com', '123456')
```

> 使用函数视图写一个功能，以json格式返回所有的用户信息:

```
//GET方式实现，page = 页码 size = 每页行数 如果非整数或者不传参数，则返回全部
http://127.0.0.1:8000/dashboard/userList/?page=1&size=20
```

views 代码如下：
```
def userList(request):
    page = request.GET.get('page')
    size = request.GET.get('size')

    if page and size and str.isnumeric(page) and str.isnumeric(size):
        p, s = int(page), int(size)
        user_data_tmp = User.objects.all()
        paginator = Paginator(user_data_tmp, s) # 使用Paginator 进行分页
        return_data = paginator.get_page(p)
    else:
        return_data = User.objects.all()

    # 处理结果，返回要求格式
    user_list = []
    for x in return_data:
        user_dict = {'username': x.username, 'email': x.email, 'id': x.id}
        user_list.append(user_dict)

    return HttpResponse(json.dumps(user_list))
```