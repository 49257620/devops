from django.http import HttpResponse, JsonResponse, QueryDict
from django.views import View
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
import logging

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("")


# 类视图
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('index view!')


class UserViewV2(View):
    def get(self, request, *args, **kwargs):
        per = 10
        page = int(kwargs.get('page'))
        page = page if page > 0 else 1
        queryset = User.objects.all()[(page - 1) * per:page * per]
        data = [{'id': user.id, 'username': user.username, 'email': user.email} for user in queryset]
        return JsonResponse(data, safe=False)


class UserInfoView(View):
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.create_user(username, email, password)

        return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email}, safe=False)


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


def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponse("用户登陆成功!")
        else:
            return HttpResponse("用户登陆失败!")

    return render(request, 'login.html')


class GroupListView(View):
    def get(self, request, *args, **kwargs):
        group_set = Group.objects.all()

        data = [{'id': group.id, 'groupname': group.name} for group in group_set]
        return JsonResponse(data, safe=False)


class GroupUserView(View):
    def get(self, request, *args, **kwargs):
        id = request.GET.get('gid')
        group = Group.objects.get(pk=id)
        user_set = group.user_set.all()
        data = [{'id': user.id, 'username': user.username, "email": user.email} for user in user_set]
        return JsonResponse(data, safe=False)


class UserGroupView(View):
    def get(self, request, *args, **kwargs):
        id = request.GET.get('uid')
        user = User.objects.get(pk=id)
        group_set = user.groups.all()
        data = [{'id': group.id, 'groupname': group.name} for group in group_set]
        return JsonResponse(data, safe=False)


class UserGroupAddView(View):
    def post(self, request, *args, **kwargs):
        uid = request.POST.get('uid')
        gid = request.POST.get('gid')
        group = Group.objects.get(pk=gid)
        user = User.objects.get(pk=uid)
        group.user_set.add(user)
        data = {'uid': user.id, 'username': user.username, 'groupid': group.id, 'groupname': group.name}
        return JsonResponse(data, safe=False)


class UserGroupDelView(View):
    def post(self, request, *args, **kwargs):
        uid = request.POST.get('uid')
        gid = request.POST.get('gid')
        group = Group.objects.get(pk=gid)
        user = User.objects.get(pk=uid)
        group.user_set.remove(user)
        data = {'uid': user.id, 'username': user.username, 'groupid': group.id, 'groupname': group.name}
        return JsonResponse(data, safe=False)


class GroupView(View):
    def post(self, request, *args, **kwargs):
        gname = request.POST.get('gname')
        t = Group.objects.filter(name=gname)
        print(t, len(t))
        if len(t) == 0:
            group = Group(name=gname)
            group.save()
            data = {'id': group.id, 'groupname': group.name}
            return JsonResponse(data, safe=False)
        else:
            return HttpResponse("已存在")
