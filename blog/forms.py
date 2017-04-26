# -*- coding: utf-8 -*-
from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')


# class UploadFileForm(forms.Form):
#     title = forms.CharField(label='Título', max_length=50)
#     text = forms.CharField(label='Texto', widget=forms.Textarea)
#     file = forms.FileField(required=False)
