from django import forms
from .models import BlogComment


class CommentForm(forms.ModelForm):

  nameFamily = forms.CharField(label='نام و نام خانوادگی', required=True)
  message    = forms.CharField(label='نظر', widget=forms.Textarea(attrs={
    'placeholder': 'نظر خود را بنویسید...'
  }), required=True)

  class Meta:
    model = BlogComment
    fields = [
      'nameFamily',
      'message'
    ]