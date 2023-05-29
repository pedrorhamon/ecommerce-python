# coding=utf-8

from django.urls import path

from . import views

app_name = 'checkout'

urlpatterns = [
    path(
        'carrinho/adicionar/(?P<slug>[\w_-]+)/', views.create_cartitem,
        name='create_cartitem'
    ),

     path('carrinho/', views.cart_item, name='cart_item')
]
