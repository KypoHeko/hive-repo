from django.shortcuts import render
from .models import Persona
#from django.http import http404

def index(request):
    return render(request, "index.html")

def main(request):
    return render(request, "main.html", {'range':range(1,12)})

def er404(request):
    return render(request, "404.html")

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
