from django.shortcuts import render
from forms import ContactForm
from models import Contact
import datetime

def register(request):
    return render(request, 'register.html', locals())

def contact(request):
    if request.POST:
        f = ContactForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            content = f.cleaned_data['content']
            email = f.cleaned_data['email']
            Contact.objects.create(name = name, email = email, content = content,
                                   date = datetime.datetime.now())
            f = ContactForm()
    else:
        f = ContactForm()

    return render(request, 'contact.html', locals())