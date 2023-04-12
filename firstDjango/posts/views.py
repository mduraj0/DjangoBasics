from django.shortcuts import render
from posts.models import Post


# def posts_list(request):
#     htlm = """<ul>"""
#     for post in Post.objects.all():
#         htlm += f'<li>{post}</li>'
#
#     htlm += "</ul>"
#     return HttpResponse(htlm)


def post_details(request):
    post = Post.objects.first()
    context = {'post': post}
    return render(request, 'posts/post_details.html', context)


def posts_list(request):
    posts = Post.objects.all()
    context = {'posts_list': posts}

    return render(request, 'posts/list.html', context)

