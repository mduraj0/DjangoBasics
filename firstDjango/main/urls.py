from django.urls import path
from .views import hello, some_test, about

app_name = 'main'

urlpatterns = [
    path('', hello, name='hello'),
    path('testy', some_test),
    path('about', about, name='about')
]