from django.urls import path
from . import  views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('score/get_score', views.keyin_score, name = 'keyin_score'),
    ]