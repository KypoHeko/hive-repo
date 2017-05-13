from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Persona
from .forms import PersonaForm
import random

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, "index.html")

def main(request):
    return render(request, "main.html")

def er404(request):
    return render(request, "404.html")

def musician(request):
    colors = ["673ab7", "5d3fb6", "5345b6", "494bb5", "3f51b5", "3067c4", "217dd4", 
              "1293e4", "03a9f4", "02adec", "01b2e4", "00b7dc", "00bcd4", "13b8b3", 
              "26b592", "39b271", "4caf50", "6cba4a", "8cc544", "acd03e", "cddc39",
              "d9df39", "e6e33a", "f2e73a", "ffeb3b", "ffd62c", "ffc11d", "ffac0e",
              "ff9800", "fd8909", "fb7f12", "f96d1b", "f75f24", "f5512d", "f44336"]
    return render(request, "musician.html", {'colors': colors})

def messages(request):
    return render(request, "messages.html")

def settings(request):
    persona = Persona.objects.get(id=31)

    if request.method == "POST":
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.save()
    else:
        form = PersonaForm(instance=persona)

    return render(request, "settings.html", {'form': form})

def communities(request):
    return render(request, "communities.html")

def gallery(request):
    return render(request, "gallery.html", {'range': range(1,28)})

def friends(request):
    return render(request, "friends.html", {'range': range(1,28)})

def id(request, pk):
    data = Persona.objects.get(id=pk)

    for _ in range(6):
        friends = Persona.objects.all().order_by('?')[:6]

    pics = []
    for _ in range(3):
        pics.append(random.randint(1, 27))

    number_list = range(1, 120)
    page = request.GET.get('page', 1)
    paginator = Paginator(number_list, 10)
    numbers = paginator.page(page)

    return render(request, "id.html", {'data': data, 'friends': friends, 'pics': pics, 
        'numbers': numbers})

def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {'form': form})

def loginform(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('main')
    return render(request, "loginform.html")
