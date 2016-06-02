# -​*- coding: UTF-8 -*​-

from django.shortcuts import render, get_object_or_404
from forms import ContactForm
import datetime
from models import Page, Article, Editor, Category, Contact

# Create your views here.
def home(request):
    page = Page.objects.get(id = 2)
    title = page.title
    h1 = title
    subtitle = page.subtitle
    post_list = Article.objects.all()

    return render(request, 'index.html', locals())

def view_single_article(request, slug):
    post_list = [get_object_or_404(Article, slug = slug)]
    return render(request, 'index.html', locals())

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