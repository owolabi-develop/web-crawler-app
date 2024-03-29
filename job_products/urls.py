from django.urls import path, include
from . import views
app_name = 'crawler'
urlpatterns = [
    path("",views.news,name='news'),
    path("Job/",views.job,name='job'),
    path("LatestBooks",views.Book_view,name='Book'),
    path("JobCsvFormat/",views.Csv_format,name='Csv_format'),
    path("NewsCsvformat/",views.News_Csv_format,name='News-Csv-format'),
    path("BooksCsvformat/",views.Books_Csv_format,name='Books-Csv-format'),
]
