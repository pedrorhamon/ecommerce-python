from django.shortcuts import render
from django.http import HttpResponse
# from catalog.models import Category

from .forms import ContactForm

def index(request):
    # context = {
    #     'categories': Category.objects.all()
    # }
    return render(request, 'index.html')


def contact(request):
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html',context)

# def product_list(request):
#     return render(request, 'product_list.html')


# def product(request):
#     return render(request, 'product.html')
