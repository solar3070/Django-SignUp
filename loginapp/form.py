from django import forms
from .models import Blog

class New(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'body']