from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('blog/', views.postlist, name='postlist'),
    path('signin/', views.signin, name='signin'),
]
