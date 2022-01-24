from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def index(request):
    return HttpResponse("<h1>Страница приложения WOMEN.</h1>")

def categories(request, cat_id):
    return HttpResponse("<h1>Статьи по категориям</h1>{cat_id}</p>")
