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
    colors = ["ff6a00", "fe9000", "feb500", "fddb00", "f9fd01", "d3fc01", "adfc01",
              "87fb01", "62fb02", "3cfa02", "17f902", "03f912", "03f937", "03f85c", 
              "03f881", "04f7a5", "04f7c9", "04f6ed", "04daf6", "05b6f5", "0592f5",
              "056ef4", "054af4", "0626f3", "0906f3", "2c06f2", "5006f2", "7307f1",
              "9607f0", "b907f0", "db08ef", "ef08e1", "ef08be", "ee089b", "ee0878"]
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
