from django.db import models
# from datetime import datetime, date, time
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_abosolute_url(self):
        return reverse('home')

class POST(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    
    def get_abosolute_url(self):
       return reverse('home')

# class CATEGORY(models.Model):
    
# Create your models here.
