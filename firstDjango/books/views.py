from django.shortcuts import render
from django.http import HttpResponse


def books_list(requests):
    return HttpResponse('Here will be my library')
