from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication_year', 'author', 'available']
    search_fields = ['title', 'description']
    list_filter = ['publication_year', 'available']


