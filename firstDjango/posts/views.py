from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Post
from .forms import PostForm


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
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse("posts:add"))
    else:
        form = PostForm()
    return render(
        request,
        "posts/add.html",
        {'form': form}
    )


def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()

    else:
        form = PostForm(instance=post)

    return render(request, "posts/add.html", {'form': form})
