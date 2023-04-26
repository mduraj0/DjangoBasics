from django.shortcuts import render
from .models import Post


def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'post': post}
    if post.published:
        context['post'] = post
    return render(request, 'posts/post_details.html', context)


def posts_list(request):
    posts = Post.objects.filter(published=True)
    context = {'posts_list': posts}

    return render(request, 'posts/list.html', context)
