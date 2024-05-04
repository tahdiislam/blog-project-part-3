from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeUserForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib import messages


# Create your views here.
def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
    return render(request, "authors/add_author.html", {"form": form, "type": "Sign Up"})


@login_required
def profile(request):
    return render(request, "authors/profile.html", {"user": request.user})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successfully')
                return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "authors/add_author.html", {"form": form, "type": "Login"})


def logout_user(request):
    logout(request)
    return redirect("login")


@login_required
def my_post(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, "authors/all_posts.html", {"posts": posts})


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = ChangeUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile")

    else:
        form = ChangeUserForm(instance=request.user)
    return render(
        request, "authors/add_author.html", {"form": form, "type": "Edit Profile"}
    )


@login_required
def change_pass(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password Change successfully")
            update_session_auth_hash(request, form.user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(request.user)
    return render(
        request, "authors/add_author.html", {"form": form, "type": "Change Password"}
    )
