from django.shortcuts import render
from django.utils import timezone
from .models import Post


def welcome(request):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/welcome.html', {'posts': queryset})

# def thumbnail(self):
#        return format_html(f'<img src="{self.photo.url}" height="50">')
#   thumbnail.allow_tags = True


# @permission_required
def postlist(request):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/postlist.html', {'posts': queryset})


def login(request):
    return render(request, 'blog/login.html')


def detail(request):
    id = request.GET.get('id', '')
    post = Post.objects.get(pk=id)
    return render(request, 'blog/detail.html', {'post': post})
