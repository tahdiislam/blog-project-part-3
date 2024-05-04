from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save(commit=True)
            return redirect("add_post")
    else:
        form = PostForm()
    return render(request, "posts/add_post.html", {"form": form})


@login_required
def edit_post(request, id):
    post = Post.objects.get(pk=id)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.instance.author = request.user
            form.save(commit=True)
            return redirect("all_posts")
    # else:
    #     form = PostForm()
    return render(request, "posts/edit_post.html", {"form": form})


@login_required
def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect("all_posts")
