from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Post
from main.forms import PostForm


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


def add_post_form(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = PostForm(request.POST)
        if form.is_valid():
            form.cleaned_data['author'] = request.user
            post = Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse("posts:add"))
    else:
        form = PostForm()
    return render(
        request,
        "posts/add.html",
        {'form': form}
    )
