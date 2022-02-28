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
    path('bbs/answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    path('bbs/comment/create/<int:question_id>', views.comment_CREATE_question, name='comment_CREATE_question'),
    path('bbs/comment/modify/<int:comment_id>', views.comment_MODIFY_question, name='comment_MODIFY_question'),
    path('bbs/comment/delete/<int:comment_id>', views.comment_DELETE_question, name='comment_DELETE_question'),
    path('bbs/comment/create/answer/<int:answer_id>/', views.comment_CREATE_answer, name='comment_CREATE_answer'),
    path('bbs/comment/modify/answer/<int:comment_id>/', views.comment_MODIFY_answer, name='comment_MODIFY_answer'),
    path('bbs/comment/delete/answer/<int:comment_id>/', views.comment_DELETE_answer, name='comment_DELETE_answer'),
]