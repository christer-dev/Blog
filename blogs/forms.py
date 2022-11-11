from django import forms

from .models import Post,Comment

class CreatePostForm(forms.ModelForm):
    title = forms.CharField(max_length =255)
    slug = forms.SlugField(max_length = 255)
    intro = forms.CharField(max_length = 300)
    body = forms.CharField(widget=forms.Textarea)
    picture = forms.ImageField(label='Profile Picture',widget=forms.FileInput)

    class Meta:
        model = Post
        fields = ['title','slug','intro','body','picture']

class UpdatePostForm(forms.ModelForm):
    title = forms.CharField(max_length =255)
    slug = forms.SlugField(max_length = 255)
    intro = forms.CharField(max_length = 300)
    body = forms.CharField(widget=forms.Textarea)
    picture = forms.ImageField(label='Profile Picture',widget=forms.FileInput)

    class Meta:
        model = Post
        fields = ['title','slug','intro','body','picture']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

