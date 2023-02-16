from django.db import models


class Book(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    publication_year = models.IntegerField()
    author = models.CharField(max_length=200)
    available = models.BooleanField(default=True)

