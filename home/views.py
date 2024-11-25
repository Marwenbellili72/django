from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def articles(request):
    return render(request, 'home/articles.html')

def contact(request):
    return render(request, 'home/contactez-nous.html') 

def services(request):
    return render(request, 'home/services.html') 

def login(request):
    return render(request, 'home/login.html')

def signup(request):
    return render(request, 'home/signup.html') 
