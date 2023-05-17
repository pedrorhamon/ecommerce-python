from typing import Any
from django.shortcuts import render;
from django.http import HttpResponse;
# from catalog.models import Category
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model


from .forms import ContactForm;

# def index(request):
#     # context = {
#     #     'categories': Category.objects.all()
#     # }
#     return render(request, 'index.html')

User = get_user_model()
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

class RegisterView(CreateView):

    form_class = UserCreationForm
    template_name = 'register.html'
    model = User
    success_url = reverse_lazy('index')


register = RegisterView.as_view()
# def product_list(request):
#     return render(request, 'product_list.html')


# def product(request):
#     return render(request, 'product.html')
