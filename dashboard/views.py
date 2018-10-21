from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.contrib.auth import authenticate, login


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
