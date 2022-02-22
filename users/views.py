from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, \
    login as django_login, authenticate
from django.contrib import auth
from users.forms import LoginForm
from django.http import HttpResponse

def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'users/login.html', {'error': 'user_name or password is incorrect.'})
    else:
        return render(request, 'users/login.html')

def logout(request):
    django_logout(request)
    return redirect('home')

def login_process(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        username = login_form.data['username']
        password = login_form.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect('home')
        else:
            return HttpResponse('로그인 실패. 다시 접속해 주세요!')