from django import forms
# class PostForm(forms.ModelForm):

#     class Meta:
#         model = Post
#         fields = ('title', 'text', 'image')


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(label='Texto', widget=forms.Textarea)
    file = forms.FileField()
