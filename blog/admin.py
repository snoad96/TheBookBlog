from django.contrib import admin
from .models import Post, Comment, Member

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Member)
