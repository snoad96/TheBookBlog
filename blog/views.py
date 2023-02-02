from django.shortcuts import render
from django.view.generic import ListView, generic

from .models import Member, Posts


class MemberList(ListView):
    model = Member


class PostList(generic.ListView):
    model = Posts
    queryset = Posts(objects.filter(status=1).order_by('-created_on'))
    template_name = 'index.html'
    paginate_by = 8
