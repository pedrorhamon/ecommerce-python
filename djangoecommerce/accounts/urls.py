# coding=utf-8

from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('alterar-dados/', views.update_user, name='update_user'),
    path('registro/', views.register, name='register')
]
