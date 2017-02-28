from django.shortcuts import render
from .models import Persona
#from django.http import http404

def index(request):
    return render(request, "index.html")

def main(request):
    return render(request, "main.html")

def er404(request):
    return render(request, "404.html")

def id(request, pk):
    data = Persona.objects.get(id=pk)

    #достаем случайные 6 записей из БД
    for _ in range(6):
        dates = Persona.objects.all().order_by('?')[:6]

    return render(request, "id.html", {'data':data, 'dates':dates})

# Create your views here.
