from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req,'home.html')

def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact.html')


def shop(req):
    return render(req,'shop.html')

def services(req):
    return render(req,'services.html')

def blog(req):
    return render(req,'blog.html')

def cart(req):
    return render(req,'cart.html')
def login(req):
    return render(req,'login.html')
