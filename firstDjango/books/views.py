from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Book
from .forms import BookForm


def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {'book': book}
    return render(request, 'books/book_detail.html', context)


def books_list(request):
    books = Book.objects.all()
    context = {'books_list': books}
    return render(request, 'books/list.html', context)


def add_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("books:add"))
    return render(
        request=request,
        template_name="books/add.html",
        context={"form": form}
    )