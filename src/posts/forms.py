from django import forms

from pagedown.widgets import PagedownWidget

from .models import Post,NewWriting

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=True))
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = [
            "title",
            'genre',
            "content",
            "image",
            "publish",
        ]

class NewWritingForm(forms.ModelForm):
    class Meta:
        model = NewWriting
        fields = [

        'title',
        'genre',
        'content',
        'join',
        ]