from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Comment


def welcome(request):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/welcome.html', {'posts': queryset})


@permission_required
def postlist(request):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/postlist.html', {'posts': queryset})


def login(request):
    return render(request, 'blog/login.html')


def detail(request):
    id = request.GET.get('id', '')
    post = Post.objects.get(pk=id)
    return render(request, 'blog/detail.html', {'post': post})


def comments(request):
    post = Post.objects.get(pk=request.POST.get('post_id'))
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return redirect('post_detail', id=post.pk)


class AddComment(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', id=post.pk)
        else:
            return redirect('post_detail', id=post.pk)