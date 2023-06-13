from django import forms
from django.contrib.auth import get_user_model

from . import models


class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']
class BlogForm(forms.ModelForm):
    edit_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Blog
        fields = ['title', 'content'] 
        User = get_user_model()


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['follows']
     
       