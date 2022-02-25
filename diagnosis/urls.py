# Diagnosis URLConf(http://127.0.0.1:8000/self_diagnosis) 자가진단
from django.urls import path
from diagnosis import views

app_name = 'diagnosis'

urlpatterns = [
    # path('', views.diagnosis, name='diagnosis'),
]