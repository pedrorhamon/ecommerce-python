from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('(?P<slug>[\w_-]+)', views.category, name='category'),
    path('produtos/(?P<slug>[\w_-]+)', views.product, name='product'),
]
