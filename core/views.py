from django.shortcuts import render

# Create your views here.
# for some reasons my github its not recognizing my commits and pushs

def index(request):
    context = {
        'curso': 'Programação Web com Django Framework'
    }
    return render(request, 'index.html', context)

def contact(request):
    contactList = {
        'client': 'Julio: (89) 91242-9562'
    }
    return render(request, 'contact.html', contactList)