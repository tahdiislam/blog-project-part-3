from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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

class AddPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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

class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/edit_post.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("profile")


@login_required
def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect("all_posts")

class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'