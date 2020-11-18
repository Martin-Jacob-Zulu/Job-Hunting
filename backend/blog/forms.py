from django import forms
from .models import BlogPost


class BlogCreateForm(forms.Form):
    class Meta:
        model = BlogPost
        fields = ("category", "image", "title", "excerpt", "content")