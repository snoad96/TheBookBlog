from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),
    path('blog/', views.postlist, name='postlist'),
    path('login/', views.signin, name='login'),
    path('accounts/', include("django.contrib.auth.urls")),
]
