from django.shortcuts import render, HttpResponse
# Create your views here.
"""

Inicio home/
Historia about/
Servicios services/
Visitanos store/
Contacto contact/
Blog blog/
Sample sample/

"""
# Create your views here.


def home(request):
    return HttpResponse("Inicio")


def about(request):
    return HttpResponse("Hitoria")


def services(request):
    return HttpResponse("Servicios")


def store(request):
    return HttpResponse("Visitanos")


def contact(request):
    return HttpResponse("Contacto")


def blog(requests):
    return HttpResponse("Blog")


def sample(requests):
    return HttpResponse("Sample")
