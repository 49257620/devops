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


class UserView(View):

    def get(self, request, *args, **kwargs):
        logger.debug("用户查询")
        per = 10
        page = 1
        if kwargs.get('page'):
            page = int(kwargs.get('page'))
        elif request.GET.get('page'):
            page = int(request.GET.get('page'))

        queryset = User.objects.all()
        paginator = Paginator(queryset, per)
        if page < paginator.page_range[0]:
            page = paginator.page_range[0]
        elif page > paginator.page_range[-1]:
            page = paginator.page_range[-1]
        paginator.page(page)
        data = [{'id': user.id, 'username': user.username, 'email': user.email} for user in
                paginator.page(page).object_list]
        return JsonResponse(data, safe=False)

    def post(self, request, *args, **kwargs):
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # email = request.POST.get('email')
        data = request.POST.dict()

        user = User.objects.create_user(**data)

        return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email}, safe=False)

    def put(self, request, *args, **kwargs):
        data = QueryDict(request.body).dict()

        user = User.objects.create_user(**data)

        return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email}, safe=False)


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
