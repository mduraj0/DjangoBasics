from django.urls import path
from .views import hello, some_test, about, contact, user_profile

app_name = 'main'

urlpatterns = [
    path('', hello, name='hello'),
    path('testy', some_test),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('user/<int:user_profile_id>/profile', user_profile, name='userprofile'),
]