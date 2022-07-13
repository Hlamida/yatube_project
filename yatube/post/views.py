from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница со списком мороженого
def group_posts(request):
    return HttpResponse('Посты по темам')
