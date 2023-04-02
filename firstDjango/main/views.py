from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def hello(request):
    return HttpResponse('Hello world')


def some_test(request):
    age = 26
    first_name = 'Michael'
    parents = ['Mom', 'Dad']
    programming_l = {
        'python' : 'advanced',
        'sql' : 'beginner',
        'ml' : 'beginner'
    }
    books = set(['Clean code', 'biblia_mysql'])
    return render(request, 'main/some_test.html', context={
        'age' : age,
        'parents' : parents,
        'programming_language' : programming_l,
        'books' : books
    })
