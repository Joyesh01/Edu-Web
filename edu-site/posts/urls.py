# filepath: /d:/EDGE web/Education-Website/edu-site/posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]