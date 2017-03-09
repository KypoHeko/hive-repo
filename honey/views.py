from django.shortcuts import render
from .models import Persona
#from django.http import http404

def index(request):
    return render(request, "index.html")

def main(request):
    return render(request, "main.html", {'range':range(1,12)})

def er404(request):
    return render(request, "404.html")

def musician(request):
    colors = ["673ab7", "5d3fb6", "5345b6", "494bb5", "3f51b5", "3067c4", "217dd4", 
              "1293e4", "03a9f4", "02adec", "01b2e4", "00b7dc", "00bcd4", "13b8b3", 
              "26b592", "39b271", "4caf50", "6cba4a", "8cc544", "acd03e", "cddc39",
              "d9df39", "e6e33a", "f2e73a", "ffeb3b", "ffd62c", "ffc11d", "ffac0e",
              "ff9800", "fd8909", "fb7f12", "f96d1b", "f75f24", "f5512d", "f44336"]
    return render(request, "musician.html", {'colors':colors})

def messages(request):
    return render(request, "messages.html")

def friends(request):
    return render(request, "friends.html")

def communities(request):
    return render(request, "communities.html")

def gallery(request):
    return render(request, "gallery.html", {'range':range(1,19)})

def id(request, pk):
    data = Persona.objects.get(id=pk)

    #достаем случайные 6 записей из БД
    for _ in range(6):
        dates = Persona.objects.all().order_by('?')[:6]

    return render(request, "id.html", {'data':data, 'dates':dates})

# Create your views here.
