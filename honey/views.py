from django.shortcuts import render
from .models import Persona

def index(request):
    return render(request, "index.html")

def main(request):
    return render(request, "main.html")

def id(request, pk):
    data = Persona.objects.get(id=pk)
    return render(request, "id.html", {'data':data})

# Create your views here.
