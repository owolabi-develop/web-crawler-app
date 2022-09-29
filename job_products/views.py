
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from . models import Book,Jobs,News

def Csv_format(request,*args,**Kwargs):
    return


def index(request):
   
    return render(request,'job_products/base.html',)

def job(request):
    url = 'https://www.python.org/jobs/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'lxml')
    job_article = soup.find('ol')
    job_list = job_article.find_all('li')
    for job in job_list:
        job_title = job.find('h2').a.string
        company = job.find('h2').a.next_sibling.next_sibling.strip()
        country = job.find('h2').span.next_sibling.next_sibling.a.string.strip()
        url = job.find('h2').span.next_sibling.next_sibling.a.get('href')
        urls = 'https://www.python.org'+url
        category = job.find('span',class_='listing-job-type').contents
        date_posted = job.find_all('time')
       
        
        job_data = Jobs()
        job_data.title = job_title
        job_data.url = urls
        for cat in category:
            job_data.desc = cat
        job_data.country = country
        job_data.company = company
        job_data.save()

        
    object_list = Jobs.objects.all()[:20]
    return render(request,'job_products/job.html',{'job':object_list})


def news(request):
    url = 'https://www.naijaloaded.com.ng/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'lxml')
    news_article = soup.find_all('article',limit=20)
    for articles in news_article:
        image = articles.img.get('src')
        url = articles.a.get('href')
        headline = articles.header.h3.a.string
        News_data = News()
        News_data.headline = headline
        News_data.url = url
        News_data.image = image
        News_data.save()
        object_list = News.objects.all()
    if headline and url and image in object_list:
            object_list.delete()
    object_list = News.objects.all()[:20]
    
    return render(request,'job_products/news.html',{'object_list':object_list})

def Book_view(request):
    url = 'http://books.toscrape.com/index.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'lxml')
    book_article = soup.find_all('article')
    for books in book_article:
        title = books.h3.a.string.strip()
        url = books.h3.a.get('href')
        images = books.img.get('src')
        price_div = books.div
        price_value = price_div.find_next_sibling('div').contents
        price = price_value[1].string.strip()

        books_data = Book()
        books_data.title = title
        books_data.url = url
        books_data.price = price
        books_data.image = images
        books_data.save()
    
    book_list = Book.objects.all()[:20]  
    return render(request,'job_products/book.html',{'book':book_list})
