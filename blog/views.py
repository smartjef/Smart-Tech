from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def service(request):
    return render(request, 'blog/paggination')