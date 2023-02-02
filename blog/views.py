from django.shortcuts import render
from django.view.generic import ListView

from .models import Member


class ListMember(ListView):
    model = Member
