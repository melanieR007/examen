from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Bienvenido")

def principal(request):
    return render(request, 'principal.html')


#http://127.0.0.1:8000/