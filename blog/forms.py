from django import forms
from .models import Comment
from django.forms import ModelForm , Textarea
from django.utils.translation import gettext_lazy as _
from captcha.fields import CaptchaField


class CommentForm(ModelForm):
  captcha = CaptchaField()
  class Meta:
    model = Comment
    fields = ["post","name" , "email" , "subject" , "message"]


