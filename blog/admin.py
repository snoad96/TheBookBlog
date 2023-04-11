from django.contrib import admin
from .models import Post

admin.site.register(Post)

admin.site.register(Comment)

admin.site.register(Member)

admin.site.register(add_comment)
