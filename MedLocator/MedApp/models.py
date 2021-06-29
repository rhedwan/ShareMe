from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse

from django.template.defaultfilters import register, slugify

# Create your models here.



class StoreCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(StoreCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def post_count(self):
        return self.posts.all().count() 

class StoreItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    store_owner  = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to = "images/", null=True, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE, related_name= 'posts', default=1)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('home')