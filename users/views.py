from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, \
    login as django_login, authenticate
from django.contrib import auth
from django.contrib.auth.models import User
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
            return render(request, 'users/login.html',)
    else:
        return render(request, 'users/login.html')

def logout(request):
    django_logout(request)
    return redirect('home')


def account(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['user_name'],
                password=request.POST['password1'],
                email=request.POST['email'], )
            auth.login(request, user)
            return redirect('/')
        return render(request, 'users/account.html')
    return render(request, 'users/account.html')