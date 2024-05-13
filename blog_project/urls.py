from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.all_post, name="homepage"),
    path("category/<slug:category_slug>/", views.all_post, name="category_wise_post"),
    path("author/", include("authors.urls")),
    path("post/", include("posts.urls")),
    path("category/", include("categories.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)