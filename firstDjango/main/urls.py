from django.urls import path
from main.views import hello

urlpatterns = [
    path('', hello)
]