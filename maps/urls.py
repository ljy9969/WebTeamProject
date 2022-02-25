from django.urls import path
from maps import views

app_name = 'map'
urlpatterns = [
    path('positions/', views.pos_hospital, name='pos_hospital')
]
