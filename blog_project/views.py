from django.shortcuts import render
from posts.models import Post
from categories.models import Category


def all_post(request, category_slug=None):
    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)
        posts = Post.objects.filter(categories=category)
        print("🐍 File: blog_project/views.py | Line: 10 | all_post ~ posts",posts)
    else:
        posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, "home.html", {"posts": posts, "categories": categories})
