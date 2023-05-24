from django.shortcuts import render;
# from catalog.models import Category
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.contrib.messages import messages

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
    elif request.method == 'POST':
         messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)

# def product_list(request):
#     return render(request, 'product_list.html')


# def product(request):
#     return render(request, 'product.html')
