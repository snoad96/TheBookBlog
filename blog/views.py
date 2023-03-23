from django.shortcuts import render
from django.utils import timezone
from .models import Post


def welcome(request):
    return render(request, 'blog/welcome.html')


def postlist(request):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/postlist.html', {'posts': queryset})

def signin(request):
    return render(request, 'blog/signin.html')
