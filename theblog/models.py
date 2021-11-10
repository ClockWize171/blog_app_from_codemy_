from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.query_utils import RegisterLookupMixin
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=120)
    title_tag = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image_field = models.ImageField(null=True, blank= True, upload_to='images/')
    body = models.TextField(null=True, blank=True)
    publish_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=120, default='uncategorized')
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} - {self.post.author}"