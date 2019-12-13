from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect
import datetime as dt
from .models import Article


# Create your views here.
# def welcome(request):
#     title = "This is my title"
#     return render(request,'welcome.html',{'title':title})


def news_of_day(request):
    date = dt.date.today()
    news = Article.todays_news()
    message = "This page should display everything and yet its not"
    return render(request,'all-news/today-news.html',{"date":date,"news":news,"message":message})



def past_days_news(request,past_date):
    
    try:

       # Converts data from string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
       # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
        
    if date == dt.date.today():
        return redirect(news_of_day)

    news =Article.days_news(date)
  
    return render(request,'all-news/past-news.html',{'date':date,"news":news})

def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        search_articles = Article.search_by_title(search_term)
        
        message = f"{search_term}"
        return render(request, 'all-news/search.html',{"message":message,"articles":search_articles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})
    
    
def article(request,article_id):
    try:
        article = Article.objects.get(id=article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html",{'article':article})