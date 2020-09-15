from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def new(request):
    return render(request, 'newpage.html', {})
