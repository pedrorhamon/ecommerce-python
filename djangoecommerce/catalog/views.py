from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Product, Category

class ProductListView(generic.ListView):

    model = Product;
    template_name = 'catalog/product_list.html'


class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html';
    context_object_name = 'product_list';

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])
    
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

# def category(request, pk=None, slug=None):
#     category = Category.objects.get(slug=slug)
#     context = {
#         'current_category': category,
#         'product_list': Product.objects.filter(category=category),
#     }
#     return render(request, 'catalog/category.html', context);

def product(request, pk=None, slug=None):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context);

product_list = ProductListView.as_view();
category = CategoryListView.as_view();
# Create your views here.
