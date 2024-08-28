from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'VegeViewApp/index.html')

def signup(request):
    return render(request, 'VegeViewApp/signup.html')

def login(request):
    return render(request, 'VegeViewApp/login.html')

def forgotpassword(request):
    return render(request, 'VegeViewApp/forgotpassword.html')
