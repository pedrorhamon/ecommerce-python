"""
URL configuration for djangoecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView

from core import views;

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contact, name='contact'),
    # path('produto/', views.product, name='product'),
    path('entrar/', LoginView.as_view(template_name='login.html'), name='login'),
    path('sair/', LogoutView.as_view(next_page='index'), name='logout'),
    # path('registro/', views.register, name='register'),
    path('catalogo/', include('catalog.urls', 'catalog')),
    path('conta/', include('accounts.urls', 'accounts')),
    path('compras/', include('checkout.urls', 'checkout')),
    path('admin/', admin.site.urls),
]
