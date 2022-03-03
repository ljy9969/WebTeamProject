from django.urls import path
from django.conf import settings
from probbs import views

app_name = 'probbs'
urlpatterns = [
    path('', views.index, name='index'),
    path('question/create/', views.question_create, name='question_create'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/comment/create/', views.create_comment, name='create_comment'),
    path('<int:question_id>/comment/delete/', views.delete_comment, name='delete_comment'),
    path('<int:question_id>/question/modify/', views.modify_question, name='modify_question'),
    path('<int:question_id>/question/delete/', views.delete_question, name='delete_question'),
    path('<int:question_id>/question/like/', views.like_question, name='like_question')

]




