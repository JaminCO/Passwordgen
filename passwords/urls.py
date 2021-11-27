from django.contrib import admin
from django.urls import path
from . import views

app_name = 'passwords'

urlpatterns = [
    path('', views.home_view, name='home'),
]