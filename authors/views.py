from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, update_session_auth_hash, login, logout
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm


# Create your views here.
def register_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = RegisterForm()
        return render(request, 'authors/add_author.html', {'form': form, 'type': 'Sign Up'})
    else:
        return redirect('profile')
    
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'authors/profile.html', {'user'})

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'authors/add_author.html', {'form': form, 'type': 'Login'})