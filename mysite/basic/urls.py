from django.contrib import admin
from django.urls import path

from . import  views

urlpatterns = [
    path('basic/', views.index, name = 'basic.index'),
]
