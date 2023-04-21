from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    sponsored = models.BooleanField(default=False)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField("tags.Tag", related_name="posts")
    categories = models.ManyToManyField(Category, related_name='posts', blank=True)

    def __str__(self):
        return f'{self.id} {self.title}'
