from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError

# Create your models here.

class Service(models.Model):
    """SQL Table that has the head field with a name of service
    and text field with a discription of the service.
    """
    head = models.CharField(max_length=50)
    text = models.TextField()


class Article(models.Model):
    """SQL table with user's articles"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})


class FeedbackMessage(models.Model):
    """SQL table for user's feedback"""
    title = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str_(self):
        return self.title
