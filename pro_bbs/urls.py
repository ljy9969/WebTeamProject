from django.urls import path
from pro_bbs import views


app_name = 'probbs'
urlpatterns = [
    path('bbs/', views.index, name='index'),
    path('bbs/<int:question_id>/', views.detail, name='detail'),
    path('bbs/answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('bbs/question/create/', views.question_create, name='question_create'),
    path('bbs/question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('bbs/question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('bbs/answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('bbs/answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete')
]