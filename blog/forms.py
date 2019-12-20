
from django import forms
from blog.models import Post, Sport, Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

class SportForm(forms.ModelForm):

    class Meta:
        model = Sport
        fields = '__all__'