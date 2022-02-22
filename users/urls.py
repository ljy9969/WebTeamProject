# Users URLConf(http://127.0.0.1:8000/users)
from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('loginProcess/', views.login_process, name='login_process'),
    path('account/', views.account, name='account'),
]