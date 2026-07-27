from django import forms
from .models import Contact ,Newsletter
from django.forms import ModelForm , Textarea
from django.utils.translation import gettext_lazy as _
from captcha.fields import CaptchaField


class NameForm(forms.Form):
  name = forms.CharField(max_length=255 )
  email = forms.EmailField(required=False)
  subject = forms.CharField(max_length=255)
  message =forms.CharField(widget=forms.Textarea)


    

class ContactForm(ModelForm):
  age = forms.IntegerField(required=False)
  captcha = CaptchaField()

  
  class Meta:
    model = Contact
    fields = '__all__'
    """ exclude = ['name','email'] """
    widgets = {
            "message": Textarea(attrs={"cols": 50, "rows": 10}),
        }

    help_texts = {
            "message": _("Tell Us about yourself."),
        }
    
    """   labels = {
          "name": _("Writer"),
      } """
"""   def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.fields['subject'].required = False """

class NewletterForm(ModelForm):
  class Meta:
    model=Newsletter
    fields = '__all__'