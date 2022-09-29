
from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    price = models.CharField(max_length=255)
    image = models.URLField(max_length=255)

    def save(self,*args,**kwargs):
        if self.title == self.title:
            self.title = self.title
        return super(Book,self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.title


class Jobs(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    url = models.URLField(max_length=255,blank=True,null=True)
    company = models.CharField(max_length=255,blank=True,null=True)
    desc = models.TextField(max_length=255,blank=True,null=True)
    country = models.CharField(max_length=255,blank=True,null=True)
    date_posted = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_posted']

    def __str__(self) -> str:
        return self.title

class News(models.Model):
    headline = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    image = models.URLField(max_length=255)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.headline
    def save(self,*args,**kwargs):
        if self.headline == self.headline:
            self.headline = self.headline
        return super(News,self).save(*args,**kwargs)

    class Meta:
        ordering = ['date_posted']
    
