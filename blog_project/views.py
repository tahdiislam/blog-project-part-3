from django.shortcuts import render
from posts.models import Post


def all_post(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})
