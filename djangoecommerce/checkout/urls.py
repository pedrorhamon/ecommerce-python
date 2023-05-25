# coding=utf-8

from django.conf.urls import path

from . import views

urlpatterns = [
    path(
        'carrinho/adicionar/(?P<slug>[\w_-]+)/', views.create_cartitem,
        name='create_cartitem'
    )
]
