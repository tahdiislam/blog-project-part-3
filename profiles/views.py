from django.shortcuts import render
from .forms import ProfileForm


# Create your views here.
def add_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm()
    return render(request, "profiles/add_profile.html", {"form": form})
