from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def books_list(requests):
    books = Book.objects.all()
    context = {'books_list': books}
    return render(requests, 'books/list.html', context)
