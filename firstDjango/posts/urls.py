from django.urls import path
from .views import posts_list, post_details


urlpatterns = [
    path('1', post_details),
    path('', posts_list),

]