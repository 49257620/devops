from django.http import HttpResponse, JsonResponse, QueryDict
from django.views import View
from django.contrib.auth.models import User
from django.core.paginator import Paginator
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



