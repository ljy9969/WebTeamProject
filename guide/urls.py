# Guide URLConf(http://127.0.0.1:8000/guide) 코로나 증상 및 행동수칙
from django.urls import path
from guide import views

app_name = 'guide'

urlpatterns = [
    path('', views.guide, name='guide'),
]