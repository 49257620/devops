from django.http import HttpResponse
from django.views import View


def index(request):
    return HttpResponse("")


# 类视图
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('index view!')


class UserView(View):
    # 支持自定义方法，方法名小写
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace', 'list']

    def get(self, request, *args, **kwargs):
        return HttpResponse('获取用户信息')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('删除用户信息')

    def post(self, request, *args, **kwargs):
        return HttpResponse('修改用户')

    def put(self, request, *args, **kwargs):
        return HttpResponse('添加用户')

    def list(self, request, *args, **kwargs):
        return HttpResponse('用户列表')
