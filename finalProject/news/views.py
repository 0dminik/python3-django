from django.shortcuts import render
from .models import News

# Create your views here.


def news_page(request, id):
    context = {}
    context['new'] = News.objects.get(id=id)
    return render(request, 'full_news_page.html', context)
