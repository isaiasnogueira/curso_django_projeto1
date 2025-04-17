from django.shortcuts import render
from django.http import HttpResponse

# function home
def home(request):
    return render(request, 'home.html')

# function contats
def contato(request):
    return HttpResponse('CONTATO')

# function on
def sobre(request):
    return HttpResponse('SOBRE')

