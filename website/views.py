from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Person

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(request, password=password, username=username)
        if user is not None:
            auth.login(request, user)
            persons = Person.objects.all()
            return render(request, 'newpage.html', {'persons':persons})
        else:
            return redirect('home')
    else:
        return render(request, 'home.html', {})

    return render(request, 'home.html', {})
