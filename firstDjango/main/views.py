from django.shortcuts import render
# from django.http import HttpResponse
from .forms import ContactForm


def hello(request):
    return render(request, 'main/hello.html')


def about(request):
    return render(request, 'main/about.html')


def some_test(request):
    age = 26
    first_name = 'Michael'
    children = ['Aniela', 'Rozalia', 'Julian']
    programming_l = {
        'python': 'advanced',
        'sql': 'beginner',
        'ml': 'beginner'
    }
    books = set(['Clean code', 'biblia_mysql'])

    return render(request, 'main/some_test.html', context={
        'age': age,
        'first_name': first_name,
        'children': children,
        'programming_l': programming_l,
        'books': books
    })


def contact(request):
    form = ContactForm()
    return render(request, "main/contact.html", {'form': form})
