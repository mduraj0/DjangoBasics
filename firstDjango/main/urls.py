from django.urls import path
from .views import hello, some_test

app_name = 'main'

urlpatterns = [
    path('', hello, name='hello'),
    path('testy', some_test)
]