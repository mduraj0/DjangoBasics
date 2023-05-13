from django.db import models
from django.utils.timezone import now, timedelta


class CheckAgeMixin:
    def is_older_than(self, n=1):
        """Check if created is older than now() - n days """
        delta = timedelta(days=n)
        return now() - self.created > delta


class Timestamped(models.Model, CheckAgeMixin):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Post(Timestamped):
    title = models.CharField(verbose_name='Tytuł' ,max_length=250)
    content = models.TextField(verbose_name='Treść')
    published = models.BooleanField(verbose_name='Opublikowany', default=False)
    sponsored = models.BooleanField(verbose_name='Sponsorowany', default=False)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField("tags.Tag", related_name="posts")
    categories = models.ManyToManyField(Category, related_name='posts', blank=True)
    example_file = models.FileField(upload_to='posts/examples/', blank=True, null=True)
    image = models.ImageField(upload_to="posts/images/%Y/%m/%d", null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.title}'
