from django.urls import path
from .views import books_list, book_detail, add_book

app_name = 'books'

urlpatterns = [
    path('<int:book_id>', book_detail, name='details'),
    path('', books_list, name='list'),
    path('add', add_book, name='add')
]
