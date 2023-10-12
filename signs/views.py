from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request, 'signs/home.html')

def sign (request):
    return render(request, 'signs/signs.html')