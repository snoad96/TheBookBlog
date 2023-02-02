from django.contrib import admin
from .models import Posts
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Posts)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')

    # admin.site.register(Posts)
