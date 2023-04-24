from django.shortcuts import render
from .models import Book


def book_detail(requests, book_id):
    book = Book.objects.get(pk=book_id)
    context = {'book': book}
    return render(requests, 'books/book_detail.html', context)


def books_list(requests):
    books = Book.objects.all()
    context = {'books_list': books}
    return render(requests, 'books/list.html', context)
