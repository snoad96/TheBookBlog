from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='blog/welcome.html'), name='welcome'),
    path('blog/', views.postlist, name='postlist'),
    path('login/', views.login, name='login'),
    path('accounts/', include("django.contrib.auth.urls")),
]
