# Diagnosis URLConf(http://127.0.0.1:8000/diagnosis) 자가진단
from django.urls import path
from diagnosis import views

app_name = 'diagnosis'

urlpatterns = [
    path('', views.s_diagnosis, name='s_diagnosis'),
    path('test/', views.my_views, name='my_views'),
]