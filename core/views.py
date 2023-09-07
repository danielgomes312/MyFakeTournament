from django.shortcuts import render

# Create your views here.
# for some reasons my github its not recognizing my commits and pushs

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')