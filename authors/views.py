from django.shortcuts import render, redirect
from .forms import AuthorForm


# Create your views here.
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_author")
    else:
        form = AuthorForm()
    return render(request, "authors/add_author.html", {"form": form})
