# Diagnosis URLConf(http://127.0.0.1:8000/diagnosis) 자가진단
from django.urls import path
from diagnosis import views

app_name = 'diagnosis'

urlpatterns = [
    path('', views.s_diagnosis, name='s_diagnosis'),
    path('<int:question_id>/', views.detail),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('<int:question_id>/results/', views.result, name='result'),
    # path('/result/', views.s_result, name='s_result'),
]