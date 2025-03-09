from django.shortcuts import render
from .models import News

def news(request):
    all_news = News.objects.all().order_by('-published_date')
    return render(request, 'news/news_list.html', {'news': all_news})
