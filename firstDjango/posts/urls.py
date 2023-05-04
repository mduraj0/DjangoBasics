from django.urls import path
from .views import posts_list, post_details, add_post_form


app_name = 'posts'

urlpatterns = [
    path('add/', add_post_form, name='add'),
    path('<int:post_id>', post_details, name='details'),
    path('', posts_list, name='list'),
]