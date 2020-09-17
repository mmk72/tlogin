from django.shortcuts import render
from .models import Person

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def new(request):
    persons = Person.objects.all()
    return render(request, 'newpage.html', {'persons':persons})
