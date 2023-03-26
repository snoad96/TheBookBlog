from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='blog/welcome.html'), name='welcome'),
    path('blog/', views.postlist, name='postlist'),
    path('login/', views.login, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='blog/login.html')),
    path('accounts/', include("django.contrib.auth.urls")),
]
