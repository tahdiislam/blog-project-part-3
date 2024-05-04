from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.all_post, name="homepage"),
    path("category/<slug:category_slug>/", views.all_post, name="category_wise_post"),
    path("author/", include("authors.urls")),
    path("post/", include("posts.urls")),
    path("category/", include("categories.urls")),
]
