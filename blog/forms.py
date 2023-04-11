from django import forms
from .models import Member


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
