from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import json
from django.core.paginator import Paginator


def index(request):
    print('Method:', request.method)
    if request.method == "GET":
        print(request.GET)
    elif request.method == "POST":
        print(request.POST)
    elif request.method == 'PUT':
        print('GET:', request.GET)
        print('POST:', request.POST)
        print('body:', request.body)
        print('QueryDict:', QueryDict(request.body))

    elif request.method == 'DELETE':
        print('GET:', request.GET)
        print('POST:', request.POST)
        print('body:', request.body)
        print('QueryDict:', QueryDict(request.body))

    return HttpResponse("")


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


def userList(request):
    page = request.GET.get('page')
    size = request.GET.get('size')

    if page and size and str.isnumeric(page) and str.isnumeric(size):
        p, s = int(page), int(size)
        user_data_tmp = User.objects.all()
        paginator = Paginator(user_data_tmp, s)
        return_data = paginator.page(p)
    else:
        return_data = User.objects.all()

    user_list = []
    for x in return_data:
        user_dict = {'username': x.username, 'email': x.email, 'id': x.id}
        user_list.append(user_dict)

    return HttpResponse(json.dumps(user_list))


def articlesInfoView(request, *args, **kwargs):
    return_dict = {'args': args, 'kwargs': kwargs}
    return JsonResponse(return_dict, safe=False)
