from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MyModel

from news.models import News

# Create your views here.


def homeView(request):
    context = {}
    context['all_news'] = News.objects.all()
    return render(request,'index.html', context)
