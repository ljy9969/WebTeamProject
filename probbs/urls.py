from django.urls import path
from probbs import views

app_name = 'probbs'
urlpatterns = [
    path('main/', views.index, name='index')
]
