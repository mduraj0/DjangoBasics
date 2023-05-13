from django.db import models
from common.models import Timestamped


class Author(Timestamped):
    name = models.CharField(max_length=200)
    birth_day = models.IntegerField()
    death_year = models.IntegerField(blank=True, null=True)
    biogram = models.TextField()

    def __str__(self):
        return f'{self.name}  ({self.birth_day} - )'


class Book(Timestamped):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publication_year = models.IntegerField()
    available = models.BooleanField(default=False)
    tags = models.ManyToManyField("tags.Tag", related_name="books")
    authors = models.ManyToManyField(Author, related_name="books")
    cover = models.ImageField(upload_to="books/covers/%Y/%m/%d", null=True, blank=True)

    def __str__(self):
        return f'{self.title} - {self.author}'
