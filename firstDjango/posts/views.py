from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post


def posts_list(request):
    htlm = """<ul>"""
    for post in Post.objects.all():
        htlm += f'<li>{post}</li>'

    htlm += "</ul>"
    return HttpResponse(htlm)


def first_post(request):
    post = Post.objects.first()
    html = '<h2>' + post.title + '</h2>'
    html += f'''<div>
        <small>Utworzono {post.created}, zmodyfikowano {post.modified} </small>
    </div>
    <div>
    <p> {post.content} </p>
    </div>'''

    return HttpResponse(html)
