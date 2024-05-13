from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


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

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('my_posts')
    pk_url_kwarg = 'id'

@method_decorator(login_required, name='dispatch')
class DetailsPostView(DetailView):
    model = Post
    template_name = 'posts/post_details.html'
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context