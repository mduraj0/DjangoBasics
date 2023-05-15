import string
from random import choice
from django.db import models
from django.utils.text import slugify
from common.models import Timestamped


def get_random_text(n):
    letters = string.ascii_letters
    return ''.join(choice(letters) for i in range(n))


class Status(models.IntegerChoices):
    NEW = 1, 'new'
    HIDE = 2, 'hide'
    PUBLISHED = 3, 'published'


class Gallery(Timestamped):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    status = models.PositiveSmallIntegerField(default=Status.NEW, choices=Status.choices)

    def save(self, *args, **kwargs):
        if self._state.adding and not self.slug:
            slug = slugify(self.title)
            slugs = self.__class__.objects.values_list('slug', flat=True)
            if slugs:
                while True:
                    if slug in slugs:
                        slug += get_random_text(5)
                    else:
                        break
            self.slug = slug
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


def upload_to(instance, filename):
    return f'galleries/{instance.gallery.slug}/{filename}'


class Photo(Timestamped):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    short_description = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to=upload_to)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name="photos")
    source = models.CharField(max_length=255, null=True, blank=True)
    status = models.PositiveSmallIntegerField(default=Status.NEW, choices=Status.choices)

    def __str__(self):
        return self.slug

    @property
    def is_published(self):
        return self.status == Status.PUBLISHED
