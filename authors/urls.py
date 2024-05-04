from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.register_user, name='add_author'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_user, name='login')
]
