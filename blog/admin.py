from django.contrib import admin
from .models import Posts
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Posts)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')

    # admin.site.register(Posts)
