from django.urls import path
from main.views import hello, some_test


urlpatterns = [
    path('', hello),
    path('testy', some_test)
]