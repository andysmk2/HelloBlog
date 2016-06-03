# -​*- coding: UTF-8 -*​-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from models import Page, Article, Editor, Category

# Create your views here.
def home(request):
    if request.POST and request.POST.get('login'):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                login_error = '您的帳號尚未啟用'
        else:
            login_error = '帳號或密碼輸入錯誤'

    else:
        form = AuthenticationForm(request)

    page = Page.objects.get(id = 1)
    title = page.title
    h1 = title
    subtitle = page.subtitle
    post_list = Article.objects.all()

    return render(request, 'index.html', locals())

def view_single_article(request, slug):
    post_list = [get_object_or_404(Article, slug = slug)]
    return render(request, 'index.html', locals())





# def login(request):
#
#     if request.user.is_authenticated():
#         return HttpResponseRedirect('/index/')
#
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#
#     user = auth.authenticate(username=username, password=password)
#
#     if user is not None and user.is_active:
#         auth.login(request, user)
#         return HttpResponseRedirect('/')
#     else:
#         return render(request, 'registration/register.html', locals())
#
# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect('/')

