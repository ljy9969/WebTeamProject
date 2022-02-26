from django.urls import path
from pro_bbs import views


app_name = 'probbs'
urlpatterns = [
    path('bbs/', views.index, name='index'),
    path('bbs/<int:question_id>/', views.detail, name='detail'),
    path('bbs/answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('bbs/question/create/', views.question_create, name='question_create')

]