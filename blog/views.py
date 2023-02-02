from django.shortcuts import render
from django.view.generic import ListView

from .models import Member


class MemberList(ListView):
    model = Member
