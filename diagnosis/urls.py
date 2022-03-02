# Diagnosis URLConf(http://127.0.0.1:8000/diagnosis) 자가진단
from django.urls import path
from diagnosis import views

app_name = 'diagnosis'

urlpatterns = [
    path('', views.s_diagnosis, name='s_diagnosis'),
    path('<int:question_id>/', views.s_detail, name='s_detail'),
    path('<int:question_id>/vote/', views.s_vote, name='s_vote'),
    path('<int:question_id>/result/', views.s_result, name='s_result'),
    # path('result/', views.s_result, name='s_result'),
]