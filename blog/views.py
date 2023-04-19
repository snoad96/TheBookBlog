from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import permission_required
from .models import Post, Comment
from .forms import CommentForm
from django.views import View


def welcome(request):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/welcome.html', {'posts': queryset})


# @permission_required
def postlist(request):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/postlist.html', {'posts': queryset})


def login(request):
    return render(request, 'blog/login.html')


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post_id)
    form = CommentForm()
    return render(request, 'blog/detail.html', {'post': post, 'comments': comments, 'form': form})


def comments(request):
    from .models import Comment
    post = Post.objects.get(pk=request.POST.get('post_id'))
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return redirect('detail', post_id=post.pk)


class AddComment(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            print('form valid')
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', post_id=post.pk)
        else:
            print('form invalid')
            return redirect('detail', post_id=post.pk)
