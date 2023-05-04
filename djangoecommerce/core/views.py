from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    texts = ['Lore Ipsum teste doloer sit ame', 'conserto dadiel edit']
    context = {
        'title': 'Django E-Commerce',
        'texts': texts
    }
    return render(request, 'index.html', context);
