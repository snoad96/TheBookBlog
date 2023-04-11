from django.db import models
from django.utils import timezone
from users.models import User
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import requests
from django.views import View
from django.shortcuts import render, redirect
from .models import Post, Comment

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    cover = models.ImageField(null=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    updated = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    @property
    def number_of_likes(self):
        return self.likes.all().count()


class Meta:
    ordering = ['-created_on']


class Member(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=50)
    age = models.IntegerField()


class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class AddComment(View):
    def post(self, request, pk):
        single_post = Post.objects.get(pk=pk)
        content = request.POST.get('addcomment')
        comment = Comment.objects.create(post=single_post, name=request.user.username, content=content)
        return redirect('post_detail', pk=pk)

    def __str__(self):
        return f"Add_Comment View"
