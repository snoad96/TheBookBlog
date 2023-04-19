from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('blog/', views.postlist, name='postlist'),
    path('login/', views.login, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='blog/login.html')),
    path('accounts/', include("django.contrib.auth.urls")),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('add_comment/<int:pk>/', views.AddComment.as_view(), name='add_comment'),
]
