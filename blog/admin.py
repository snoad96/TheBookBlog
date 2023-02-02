from django.contrib import admin
from .models import Posts, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Posts)
class PostAdmin(SummernoteModelAdmin):

    search_fields = ('title', 'slug', 'book', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('book', 'name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approve=True)
