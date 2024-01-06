from django.shortcuts import render
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
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def store(request):
    return render(request, 'core/store.html')


def contact(request):
    return render(request, 'core/contact.html')


def sample(requests):
    return render(requests, 'core/sample.html')
