from django import forms 
from .models import Post, Comment

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('title', 'caption', 'image')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)