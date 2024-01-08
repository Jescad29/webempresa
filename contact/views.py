from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
# Create your views here.


def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Suponemos que todo ha ido bien, redireccionamos
            return redirect(reverse('contact')+"?ok")

    return render(request, 'contact/contact.html', {'form': contact_form})
