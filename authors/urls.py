from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("add/", views.register_user, name="register"),
    path("profile/", views.profile, name="profile"),
    # path("login/", views.login_user, name="login"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    # path("logout/", views.UserLogoutView.as_view(http_method_names = ['post']), name="logout"),
    path("my-posts/", views.my_post, name="my_posts"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("change-password/", views.change_pass, name="change_pass"),
]
