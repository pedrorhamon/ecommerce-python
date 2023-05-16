from typing import Any
from django.shortcuts import render;
from django.http import HttpResponse;
# from catalog.models import Category
from django.views.generic import View, TemplateView

from .forms import ContactForm;

# def index(request):
#     # context = {
#     #     'categories': Category.objects.all()
#     # }
#     return render(request, 'index.html')

class IndexView(TemplateView):

    template_name = 'index.html';

index = IndexView.as_view();


def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)

# def product_list(request):
#     return render(request, 'product_list.html')


# def product(request):
#     return render(request, 'product.html')
