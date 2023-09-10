from django.shortcuts import render

# Create your views here.
# for some reasons my github its not recognizing my commits and pushs

def index(request):
    print(dir(request.user))
    print(dir(request.body.__add__.__str__))
    print(f"User-Agent: {request.headers['User-Agent']}")

    if str(request.user) == 'danielgomes@gmail.com.br':
        teste = 'Usuário logado'
    else:
        teste = 'Usuário não logado'

    context = {
        'curso': 'Programação Web com Django Framework',
        'logado': teste
    }
    return render(request, 'index.html', context)

def contact(request):
    contactList = {
        'client': 'Julio: (89) 91242-9562'
    }
    return render(request, 'contact.html', contactList)