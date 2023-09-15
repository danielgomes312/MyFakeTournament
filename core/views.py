from django.shortcuts import render
from .models import Produto

# Create your views here.
# for some reasons my github its not recognizing my commits and pushs / problem solved

def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação Web com Django Framework',
        'produtos': produtos,
    }
    return render(request, 'index.html', context)

def contact(request):
    contactList = {
        'client': 'Julio: (89) 91242-9562'
    }
    return render(request, 'contact.html', contactList)