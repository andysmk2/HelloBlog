# -*- coding: UTF-8 -*-
from django.shortcuts import render

# Create your views here.
def home(request):
    title = 'Good Night'
    h1 = 'HAHAHA'
    content = '''
    一二三
    '''

    return render(request, 'index.html', locals())

